class Operation:
    def __init__(self, subject, verb, obj, *args):
        self.subject = subject
        self.verb = verb
        self.obj = obj
        self.args = args


class hw(Operation):
    def convert(self):
        print("Convert")
    def graph(self):
        print("Graph")
    def report(self):
        print("Report")
        
    commands = {"convert":convert, "graph":graph, "report":report}
    
    def execute(self):
        self.commands[self.verb](self)
    
    
input_user = hw('hw', 'convert', 'attack')

input_user.execute()
