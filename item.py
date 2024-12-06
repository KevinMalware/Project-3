class Item:
    """
    Represents an item with a name, description, and weight.
    """

    def __init__(self, name, desc, weight):
        """
        Initializes an item instance with name, description, and weight.

        Args:
            name (str): The name of the item.
            desc (str): The description of the item.
            weight (float): The weight of the item.
        """
        self.name = name
        self.desc = desc
        self.weight = weight

    def __str__(self):
        """
        Returns the description of the item.

        Returns:
            str: The description of the item.
        """
        return self.desc

    def get_name(self):
        """
        Gets the name of the item.

        Returns:
            str: The name of the item.
        """
        return self.name

    def get_description(self):
        """
        Gets the description of the item.

        Returns:
            str: The description of the item.
        """
        return self.desc

    def get_weight(self):
        """
        Gets the weight of the item.

        Returns:
            float: The weight of the item.
        """
        return self.weight

    def set_name(self, name):
        """
        Sets a new name for the item.

        Args:
            name (str): The new name for the item.
        """
        self.name = name

    def set_desc(self, desc):
        """
        Sets a new description for the item.

        Args:
            desc (str): The new description for the item.
        """
        self.desc = desc

    def set_weight(self, wt):
        """
        Sets a new weight for the item.

        Args:
            wt (float): The new weight for the item.
        """
        self.weight = wt
