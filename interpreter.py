import erql


def interpret(user_input):
    virtual = {'analyse' : erql.virtual_analyse()}
    clean = user_input.split(" > ")
    if clean[0] == 'cv':
        virtual[int(clean[1])]()
