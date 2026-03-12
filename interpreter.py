input_user = input("Enter ERQL: \n")

# User inputs are divided into the familiar SVO + modifier template that language teachers are already familiar with so that they understand what it is that they're asking the program to do.
class Render:
    def __init__(self, render):
        
        rendered = render.split(">")
        self.subject = rendered[0]
        self.verb = rendered[1]
        self.obj = rendered[2]
        self.mod = rendered[3:]
        

decode = Render(input_user)

if decode.subj == "hw":
    pass

if decode.subj == "cv":
    pass

if decode.subj == "personal":
    pass

if decode.subj == "groups":
    pass


