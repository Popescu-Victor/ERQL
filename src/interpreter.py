# User inputs are divided into the familiar SVO + modifier template that language teachers are already familiar with so that they understand what it is that they're asking the program to do.
class Parsed_input:
    def __init__(self, user_input):
        
        parsed = user_input.split(">")
        self.subject = user_input[0]
        self.verb = user_input[1]
        self.obj = user_input[2:]