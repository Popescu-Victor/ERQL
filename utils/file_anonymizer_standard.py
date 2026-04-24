import os
import random
import string


def file_anonymizer(folder):

    def random_string(length=12):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        
        if not os.path.isfile(filepath):
            continue
        
        ext = os.path.splitext(filename)[1] 
        new_name = random_string() + ext
        new_path = os.path.join(folder, new_name)
        
        os.rename(filepath, new_path)
        print(f"{filename} → {new_name}")