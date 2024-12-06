class Room:
    """
    Represents a room in a text-based adventure game.
    
    Attributes:
        desc (str): Short description of the room.
        equippable (Item or None): The item available in the room, if any.
        character (NPC or None): The character present in the room, if any.
        neighbors (dict): Dictionary of neighboring rooms in different directions.
    """

    def __init__(self, desc, equippable=None, character=None):
        """
        Initializes a Room object with a description, optional item, and optional character.
        
        Args:
            desc (str): Description of the room.
            equippable (Item, optional): Item in the room. Defaults to None.
            character (NPC, optional): Character in the room. Defaults to None.
        """
        self.desc = desc
        self.equippable = equippable
        self.character = character
        self.neighbors = {}

    def get_description(self):
        """
        Returns the description of the room.
        
        Returns:
            str: The description of the room.
        """
        return self.desc

    def get_item(self):
        """
        Returns the item in the room, if any.
        
        Returns:
            Item or None: The item present in the room.
        """
        return self.equippable

    def get_npc(self):
        """
        Returns the character in the room, if any.
        
        Returns:
            NPC or None: The character present in the room.
        """
        return self.character

    def set_item(self, equippable):
        """
        Sets the item present in the room.
        
        Args:
            equippable (Item): The item to place in the room.
        """
        self.equippable = equippable

    def set_npc(self, npc):
        """
        Sets the character present in the room.
        
        Args:
            npc (NPC): The character to place in the room.
        """
        self.character = npc

    def add_neighbor(self, direction, room):
        """
        Adds a neighboring room in a specified direction.
        
        Args:
            direction (str): Direction of the neighboring room (e.g., 'south').
            room (Room): The neighboring room to add.
        """
        self.neighbors[direction] = room

    def get_neighbor(self, direction):
        """
        Returns the neighboring room in the given direction, if any.
        
        Args:
            direction (str): The direction to check for a neighboring room.
        
        Returns:
            Room or None: The neighboring room if it exists, otherwise None.
        """
        return self.neighbors.get(direction, None)

    def has_item(self):
        """
        Checks if the room has an item.
        
        Returns:
            bool: True if the room has an item, False otherwise.
        """
        return self.equippable is not None

    def has_npc(self):
        """
        Checks if the room has a character.
        
        Returns:
            bool: True if the room has a character, False otherwise.
        """
        return self.character is not None

    def remove_item(self):
        """
        Removes and returns the item from the room.
        
        Returns:
            Item or None: The removed item if it existed, otherwise None.
        """
        item = self.equippable
        self.equippable = None
        return item

    def __str__(self):
        """
        Returns a string representation of the room, including its description,
        item, and character (if present).
        
        Returns:
            str: The string description of the room.
        """
        description = f"You are {self.desc}."
        if self.equippable:
            description += f"\nYou see {self.equippable}."
        if self.character:
            description += f"\nYou meet {self.character.get_name()}."
        return description
