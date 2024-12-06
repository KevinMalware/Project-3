class NPC:
    """
    A class to represent a Non-Player Character (NPC).
    
    Attributes:
    -----------
    name : str
        The name of the NPC.
    phrase : str
        The phrase spoken by the NPC.
    """

    def __init__(self, name, phrase):
        """
        Constructs all the necessary attributes for the NPC object.
        
        Parameters:
        -----------
        name : str
            The name of the NPC.
        phrase : str
            The phrase spoken by the NPC.
        """
        self.name = name
        self.phrase = phrase

    def get_name(self):
        """
        Returns the name of the NPC.

        Returns:
        --------
        str : The name of the NPC.
        """
        return self.name

    def get_phrase(self):
        """
        Returns the phrase spoken by the NPC.

        Returns:
        --------
        str : The phrase spoken by the NPC.
        """
        return self.phrase

    def set_name(self, name):
        """
        Sets/updates the name of the NPC.

        Parameters:
        -----------
        name : str
            The new name for the NPC.
        """
        self.name = name

    def set_phrase(self, phrase):
        """
        Sets/updates the phrase spoken by the NPC.

        Parameters:
        -----------
        phrase : str
            The new phrase for the NPC.
        """
        self.phrase = phrase

    def speak(self):
        """
        Returns a formatted string of the NPC speaking.

        Returns:
        --------
        str : A string containing the NPC's name and their phrase.
        """
        return f'{self.name} says, "{self.phrase}"'
