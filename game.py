from item import Item
from npc import NPC
from room import Room
import random
#first you need to import the item, npc, and room classes and import random
#so you can use them later in the game.py

class Game:

    #a constructor that initalizes the game class, in this constructor
    #there is are holders for the inventory of the player, as well as the current room of the player
    #, a message that is going to show up to the player, the previous room of the player was in, the number of
    #turns that player has taken, and there is also a create function that creates the world with
    #lastly a welcome message
    def __init__(self):
        self.items = []
        self.current = None
        self.msg = ""
        self.previous_room = None
        self.turns = 0
        self.create_world()
        self.set_welcome_message()

    #a function is being made for the game world that has different parts of the game
    def create_world(self):

        #the following below are items that are in the games, with its name, description, and weight in the parameters
        self.treasure_chest = Item("treasure chest", "a chest that will give you wealth", 100)
        self.map = Item("map", "a map that lets you skip 2 levels", 5)
        self.teleporter = Item("teleporter", "a teleporter that will randomly transport you to a level (1-8)", 30)
        self.speedy_cola = Item("speedy cola", "a drink that lets you move twice in one turn", 2)
        self.power_shield = Item("power shield", "a shield that protects you from traps in Level 6", 15)
        self.magic_key = Item("magic key", "a key that unlocks hidden shortcuts in Levels 5 and 7", 10)

        #these are the non-playable characters(npcs) that the player will be able to talk to
        #they have the name of the npc and phrase in the parameters
        self.builderman = NPC("Builderman", "Find the map and it will decrease your journey!")
        self.telamon = NPC("Telamon", "Find the chest and you will be forever rich.")
        self.noob = NPC("Noob", "Use the power shield to avoid traps ahead!")

        #these are all the levels with the description of the room and whether or not if
        #it it has a npc or item in the room within the parameters
        self.level1 = Room("a dark room with glow lights everywhere", None, self.builderman)
        self.level2 = Room("a room filled with speed boost power-ups", self.speedy_cola)
        self.level3 = Room("a misty room with mysterious fog", self.magic_key, self.telamon)
        self.level4 = Room("a lava-themed room with floating platforms", self.map)
        self.level5 = Room("a maze-like room with multiple pathways", self.power_shield, self.noob)
        self.level6 = Room("a shimmering room with hidden traps", self.teleporter)
        self.level7 = Room("a cold room with icy floors")
        self.level8 = Room("a grand hall with a glowing exit door", self.treasure_chest)

        #all the rooms are connected to another room with the direction being south of another
        self.level1.add_neighbor("south", self.level2)
        self.level2.add_neighbor("south", self.level3)
        self.level3.add_neighbor("south", self.level4)
        self.level4.add_neighbor("south", self.level5)
        self.level5.add_neighbor("south", self.level6)
        self.level6.add_neighbor("south", self.level7)
        self.level7.add_neighbor("south", self.level8)

        #you start the game at level 1 with this statement
        self.current = self.level1

    #this shows the game message
    def get_message(self):
        return self.msg

    #this shows the current room the player is in
    def get_current_room(self):
        return self.current

    #this function moves the player to antoher room in the given direction
    def move(self, direction):
        #this finds out if there is a certain room in a direction that the player
        #wants to go to
        next_room = self.current.get_neighbor(direction)

        #if there is no room, the player will be told that they can't move in that direction
        #otherwise if there is a room, the player will be moved there, also in this function
        #the previous room is being updated as well as the current room, the turn is being counted
        #, the game is being checked if it's gameover and the new room is being displayed via message
        if next_room is None:
            self.msg = "You can't move in that direction."
        else:
            self.previous_room = self.current
            self.current = next_room
            self.msg = str(self.current)
            self.turns += 1
            if self.game_over():
                return

    #in this function this is the welcoming message to the game
    def set_welcome_message(self):
        self.msg = "Welcome to the Quest Game! Escape the ROBLOX obby maze in the fewest turns possible."

    #this tells what the current room looks like through a description
    def look(self):
        self.msg = str(self.current)

    #this shows all the moves that the player can do in the game
    #ex - move certain direction, look, take, place a item, speak, use an item
    #gamble, retreat, help, or quit, as well as the objective of the game
    def help(self):
        self.msg = (
            "Commands: move <direction>, look, take, place <item>, items, speak, use <item>, "
            "gamble <odd/even>, retreat, help, quit.\nObjective: Escape by reaching Level 8."
        )

    #this shows what the items the player are holder, it is also checking if the player is holding
    #any items or if they aren't, they are told they aren't holding any items
    def items(self):
        if self.items:
            item_list = ", ".join([item.get_name() for item in self.items])
            self.msg = f"You are holding: {item_list}."
        else:
            self.msg = "You are not holding any items."

    #this lets the player pick up an item and place it in their
    #inventory, first it checks if there is item to take
    #then checks if the item is too heavy to pick up, otherwise they take item
    def take(self):
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

    #this places the item from the player's inventory in the current room
    #first it checks if they're holding aw item, then checks if there is
    #an item already in the room, otherwise the player puts an item in the room
    def place(self, item_name):
        item = self.search_items(item_name)
        if not item:
            self.msg = f"You are not holding a {item_name}."
        elif self.current.has_item():
            self.msg = "There is already an item in the room."
        else:
            self.items.remove(item)
            self.current.set_item(item)
            self.msg = f"You carefully place the {item_name} in the room."

    #this searches for the item in the player's inventory through name
    def search_items(self, name):
        for item in self.items:
            if item.get_name() == name:
                return item
        return None

    #this let the player talk to the NPC, it first checks if there is not a NPC is in the room
    #if there is aw npc, the player speaks to the NPC
    def speak(self):
        if not self.current.has_npc():
            self.msg = "There is no one here to speak to."
        else:
            npc = self.current.get_npc()
            self.msg = npc.speak()

    #this lets the player move to room they were in before
    #if there isn't a previous room or if the player is in the starting room, they're aren't
    #able to retreat, otherwise they can retreat
    def retreat(self):
        if self.previous_room is None or self.current == self.level1:
            self.msg = "You cannot retreat from here."
        else:
            self.current = self.previous_room
            self.previous_room = None
            self.msg = f"You retreated. {self.current.get_description()}"

    #this let the player use an item, first checks if they're holding an item, then
    #checks if the player is holding the useable items (speedy cola, powershield, and teleporter),
    #if they have them, they're able to use them to benefit them in the game
    #otherwise the player is let known that they can't use the item at moment
    #the speedy cola lets the player move twice in one turn and the teleporter teleports the player to a random level
    #,the power shield protects the player sfrom traps 
    def use(self, item_name):
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

    #this is a gambling action that lets the player roll a dice, if they win they move forward
    #and if they lose they go the previous level, the player picks between odds and even from
    #the range of a 1-6 dice
    def gamble(self, choice):
        roll = random.randint(1, 6)
        if (roll % 2 == 0 and choice == "even") or (roll % 2 == 1 and choice == "odd"):
            self.msg = f"You gambled and won! You skip this level."
            self.move("south")
        else:
            self.msg = f"You gambled and lost! Returning to the previous level."
            self.retreat()

    #this checks if the game is over, if the player is in level 8 they win the game
    #it also checks if they exceeded 15 turns which means they lost the game
    def game_over(self):
        if self.current == self.level8:
            self.msg = "Congratulations! You have reached the exit and won the game!"
            return True
        elif self.turns > 15:
            self.msg = "You have exceeded the maximum number of turns. Game over!"
            return True
        return False

    #this moves the player to the winning level automatically
    def auto_win(self):
        self.msg = "Starting auto-win sequence..."
        self.current = self.level8
        self.msg += " Game won successfully!"

    #this reads what player types and enters it into a command
    def parse_command(self):
        words = input("Enter>>> ").strip().split()
        if not words:
            return None, None
        command = words[0]
        arg = words[1] if len(words) > 1 else None
        return command, arg

    #this starts the game loop where the player is able to type and enter stuff to play
    #this also shows all the valid commands
    def play(self):
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

#this starts the game
if __name__ == '__main__':
    g = Game()
    g.play()
