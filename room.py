class Room:

    #we first use a constructor for room class with the attrributes being
    #desc, which is the description but shortened, as well as equippable and character
    def __init__(self, desc, equippable=None, character=None):
        self.desc = desc
        self.equippable = equippable
        self.character = character
        self.neighbors = {}

    #we use a getter method to get the description, item, and npc if there is a
    #item or npc
    def get_description(self):
        return self.desc

    def get_item(self):
        return self.equippable

    def get_npc(self):
        return self.character

    #we use a setter method to update the item and npc
    def set_item(self, equippable):
        self.equippable = equippable

    def set_npc(self, npc):
        self.character = npc

    #we use a add method to add a neighbor in the given direction
    #which will be always south
    def add_neighbor(self, direction, room):
        self.neighbors[direction] = room

    #we get the neighbor function
    def get_neighbor(self, direction):
        return self.neighbors.get(direction, None)

    #we check if there is a item has a item or npc in the following 2 methods
    def has_item(self):
        return self.equippable is not None

    def has_npc(self):
        return self.character is not None

    #this method removes an item from the room, then is returned
    def remove_item(self):
        item = self.equippable
        self.equippable = None
        return item

    #this string function checks if there is an item, it is added to the description
    #it also checks if there is a character, it gets added to the description as well
    def __str__(self):
        description = f"You are {self.desc}."
        if self.equippable:
            description += f"\nYou see {self.equippable}."
        if self.character:
            description += f"\nYou meet {self.character.get_name()}."
        return description
