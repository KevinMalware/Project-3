class Item:

    #is a constructor for the item class, this initializes the item class with
    #name, description, and weight
    def __init__(self, name, desc, weight):
        self.name = name
        self.desc = desc
        self.weight = weight

    #then we have to return the description, to use later
    def __str__(self):
        return self.desc

    #we use a get method for for the next three functions to get
    #the attributes of the item
    def get_name(self):
        return self.name

    def get_description(self):
        return self.desc

    def get_weight(self):
        return self.weight

    #we use a setter method to update the attributes
    def set_name(self, name):
        self.name = name

    def set_desc(self, desc):
        self.desc = desc

    def set_weight(self, wt):
        self.weight = wt
