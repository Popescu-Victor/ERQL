import util
from operations_class import Operation

def interpret(user_input):
    input_list = user_input.split('>')
    product = Operation(*input_list)
    return product
