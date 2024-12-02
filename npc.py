class NPC:

    #we use a constructor for the npc class with the attributes of name and phrase
    def __init__(self, name, phrase):
        self.name = name
        self.phrase = phrase

    #we use a get method to get the name and phrase of the NPC
    def get_name(self):
        return self.name

    def get_phrase(self):
        return self.phrase

    #we use a setter method to update the name and phrase of the NPC
    def set_name(self, name):
        self.name = name

    def set_phrase(self, phrase):
        self.phrase = phrase

    #we have a speak method by returning a string with the name and phrase
    def speak(self):
        return f'{self.name} says, "{self.phrase}"'
