# User inputs are divided into the familiar SVO + modifier template that language teachers are already familiar with so that they understand what it is that they're asking the program to do.
class Parsed_input:
    def __init__(self, user_input):
        
        command_list = user_input.split(">")
        self.subject = command_list[0]
        self.verb = command_list[1]
        self.obj = command_list[2:]
        self.input_as_list = [self.subject , self.verb , self.obj]