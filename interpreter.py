input_user = input("Enter ERQL: \n")


class Render:
    def __init__(self, render):
        
        rendered = render.split(">")
        self.subject = rendered[0]
        self.verb = rendered[1]
        self.obj = rendered[2]
        self.mod = rendered[3:]
        

decode = Render(input_user)

print(decode.verb)
