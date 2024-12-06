from item import Item
from npc import NPC
from room import Room
import random

class Game:
    """
    A class to represent the main game logic.

    Attributes
    ----------
    items : list
        A list to store player's inventory items.
    current : Room
        The current room the player is in.
    msg : str
        A message to display to the player.
    previous_room : Room
        The previous room the player was in.
    turns : int
        The number of turns the player has taken.

    Methods
    -------
    create_world():
        Creates the game world, including items, NPCs, and rooms.
    set_welcome_message():
        Sets the welcome message for the game.
    get_message():
        Returns the current message for the player.
    get_current_room():
        Returns the current room.
    move(direction):
        Moves the player to the next room in a given direction.
    look():
        Sets the message to describe the current room.
    help():
        Sets the message to display the available commands.
    items():
        Sets the message to list the items the player is holding.
    take():
        Adds an item in the current room to the player's inventory.
    place(item_name):
        Places an item from the player's inventory into the current room.
    search_items(name):
        Searches for an item in the player's inventory by name.
    speak():
        Allows the player to interact with an NPC if one is present.
    retreat():
        Allows the player to return to the previous room.
    use(item_name):
        Uses a specific item from the player's inventory.
    gamble(choice):
        Lets the player gamble to move forward or return to a previous room.
    game_over():
        Checks if the game is over (either won or lost).
    auto_win():
        Automatically moves the player to the winning level.
    parse_command():
        Reads player input and parses it into a command and an argument.
    play():
        Starts the game loop where the player can enter commands.
    """

    def __init__(self):
        """Initializes the game state."""
        self.items = []
        self.current = None
        self.msg = ""
        self.previous_room = None
        self.turns = 0
        self.create_world()
        self.set_welcome_message()

    def create_world(self):
        """Creates the items, NPCs, and rooms in the game."""

        # Create items with name, description, and weight
        self.treasure_chest = Item("treasure chest", "a chest that will give you wealth", 100)
        self.map = Item("map", "a map that lets you skip 2 levels", 5)
        self.teleporter = Item("teleporter", "a teleporter that will randomly transport you to a level (1-8)", 30)
        self.speedy_cola = Item("speedy cola", "a drink that lets you move twice in one turn", 2)
        self.power_shield = Item("power shield", "a shield that protects you from traps in Level 6", 15)
        self.magic_key = Item("magic key", "a key that unlocks hidden shortcuts in Levels 5 and 7", 10)

        # Create NPCs with name and phrase
        self.builderman = NPC("Builderman", "Find the map and it will decrease your journey!")
        self.telamon = NPC("Telamon", "Find the chest and you will be forever rich.")
        self.noob = NPC("Noob", "Use the power shield to avoid traps ahead!")

        # Create rooms with description, item, and NPC
        self.level1 = Room("a dark room with glow lights everywhere", None, self.builderman)
        self.level2 = Room("a room filled with speed boost power-ups", self.speedy_cola)
        self.level3 = Room("a misty room with mysterious fog", self.magic_key, self.telamon)
        self.level4 = Room("a lava-themed room with floating platforms", self.map)
        self.level5 = Room("a maze-like room with multiple pathways", self.power_shield, self.noob)
        self.level6 = Room("a shimmering room with hidden traps", self.teleporter)
        self.level7 = Room("a cold room with icy floors")
        self.level8 = Room("a grand hall with a glowing exit door", self.treasure_chest)

        # Connect rooms
        self.level1.add_neighbor("south", self.level2)
        self.level2.add_neighbor("south", self.level3)
        self.level3.add_neighbor("south", self.level4)
        self.level4.add_neighbor("south", self.level5)
        self.level5.add_neighbor("south", self.level6)
        self.level6.add_neighbor("south", self.level7)
        self.level7.add_neighbor("south", self.level8)

        # Start the game in Level 1
        self.current = self.level1

    def get_message(self):
        """Returns the current game message."""
        return self.msg

    def get_current_room(self):
        """Returns the current room the player is in."""
        return self.current

    def move(self, direction):
        """Moves the player in the given direction."""
        next_room = self.current.get_neighbor(direction)
        if next_room is None:
            self.msg = "You can't move in that direction."
        else:
            self.previous_room = self.current
            self.current = next_room
            self.msg = str(self.current)
            self.turns += 1
            if self.game_over():
                return

    def set_welcome_message(self):
        """Sets the welcome message for the game."""
        self.msg = "Welcome to the Quest Game! Escape the ROBLOX obby maze in the fewest turns possible."

    def look(self):
        """Sets the message to describe the current room."""
        self.msg = str(self.current)

    def help(self):
        """Sets the message to display available commands and the game objective."""
        self.msg = (
            "Commands: move <direction>, look, take, place <item>, items, speak, use <item>, "
            "gamble <odd/even>, retreat, help, quit.\nObjective: Escape by reaching Level 8."
        )

    def items(self):
        """Sets the message to list the items in the player's inventory."""
        if self.items:
            item_list = ", ".join([item.get_name() for item in self.items])
            self.msg = f"You are holding: {item_list}."
        else:
            self.msg = "You are not holding any items."

    def take(self):
        """Adds an item in the current room to the player's inventory."""
        if not self.current.has_item():
            self.msg = "There is nothing to take."
        else:
            item = self.current.get_item()
            if item.get_weight() > 50:
                self.msg = f"The {item.get_name()} is too heavy to pick up!"
            else:
                self.items.append(item)
                self.current.remove_item()
                self.msg = f"You are now holding the {item.get_name()}."

    def place(self, item_name):
        """Places an item from the player's inventory into the current room."""
        item = self.search_items(item_name)
        if not item:
            self.msg = f"You are not holding a {item_name}."
        elif self.current.has_item():
            self.msg = "There is already an item in the room."
        else:
            self.items.remove(item)
            self.current.set_item(item)
            self.msg = f"You carefully place the {item_name} in the room."

    def search_items(self, name):
        """Searches for an item in the player's inventory by name."""
        for item in self.items:
            if item.get_name() == name:
                return item
        return None

    def speak(self):
        """Allows the player to interact with an NPC if one is present in the room."""
        if not self.current.has_npc():
            self.msg = "There is no one here to speak to."
        else:
            npc = self.current.get_npc()
            self.msg = npc.speak()

    def retreat(self):
        """Allows the player to return to the previous room."""
        if self.previous_room is None or self.current == self.level1:
            self.msg = "You cannot retreat from here."
        else:
            self.current = self.previous_room
            self.previous_room = None
            self.msg = f"You retreated. {self.current.get_description()}"

    def use(self, item_name):
        """Uses a specific item from the player's inventory."""
        item = self.search_items(item_name)
        if not item:
            self.msg = f"You are not holding a {item_name}."
            return
        if item_name == "speedy cola":
            self.msg = "You used the Speedy Cola! You can move twice in one turn."
            self.turns -= 1
        elif item_name == "teleporter":
            self.msg = "You used the Teleporter! Transporting to a random level..."
            self.current = random.choice(
                [self.level1, self.level2, self.level3, self.level4, self.level5, self.level6, self.level7, self.level8]
            )
        elif item_name == "power shield":
            self.msg = "You used the Power Shield! You are now protected from traps."
        else:
            self.msg = f"The {item_name} cannot be used right now."

    def gamble(self, choice):
        """Lets the player gamble to move forward or return to a previous room."""
        roll = random.randint(1, 6)
        if (roll % 2 == 0 and choice == "even") or (roll % 2 == 1 and choice == "odd"):
            self.msg = f"You gambled and won! You skip this level."
            self.move("south")
        else:
            self.msg = f"You gambled and lost! Returning to the previous level."
            self.retreat()

    def game_over(self):
        """Checks if the game is over by either reaching the exit or exceeding max turns."""
        if self.current == self.level8:
            self.msg = "Congratulations! You have reached the exit and won the game!"
            return True
        elif self.turns > 15:
            self.msg = "You have exceeded the maximum number of turns. Game over!"
            return True
        return False

    def auto_win(self):
        """Automatically moves the player to the winning level."""
        self.msg = "Starting auto-win sequence..."
        self.current = self.level8
        self.msg += " Game won successfully!"

    def parse_command(self):
        """Reads player input and parses it into a command and an argument."""
        words = input("Enter>>> ").strip().split()
        if not words:
            return None, None
        command = words[0]
        arg = words[1] if len(words) > 1 else None
        return command, arg

    def play(self):
        """Starts the game loop where the player can enter commands."""
        print(self.get_message())
        while True:
            command, arg = self.parse_command()
            if command == "quit":
                print("Thank you for playing!")
                break
            elif command == "move":
                self.move(arg)
            elif command == "look":
                self.look()
            elif command == "help":
                self.help()
            elif command == "items":
                self.items()
            elif command == "take":
                self.take()
            elif command == "place":
                self.place(arg)
            elif command == "speak":
                self.speak()
            elif command == "retreat":
                self.retreat()
            elif command == "use":
                self.use(arg)
            elif command == "gamble":
                self.gamble(arg)
            elif command == "auto_win":
                self.auto_win()
            else:
                self.msg = "Unknown command. Type 'help' for a list of commands."
            print(self.get_message())

if __name__ == '__main__':
    g = Game()
    g.play()
