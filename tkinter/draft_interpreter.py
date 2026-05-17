#from src import erql
#from utils import help

# Compared if-statement to match-case statements.

def interpret(user_input):
    input_list = user_input.split(">")
    match user_input[0]:
        case "stats":
            print(input_list[0] + ' and ' + input_list[1])
        case "file":
            pass
        case "clear":
            pass
        case "graph":
            pass
        case "ilias":
            pass
        case "copy":
            pass
        case "save":
            pass


user_input = input("Write input here:   ")
interpret(user_input=user_input)