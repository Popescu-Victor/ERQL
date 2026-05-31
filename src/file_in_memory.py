# Referencing files by filepath by all functions after being uploaded through 'file>upload'.

class Filepath:
    def __init__(self, filepath):
        self.filepath = filepath
        
    def __repr__(self):
        return self.filepath
    
