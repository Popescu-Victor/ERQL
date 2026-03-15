import os

folder = r"C:\Users\roman\Desktop\Colab"

files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

for i, filename in enumerate(files, start=1):
    filepath = os.path.join(folder, filename)
    if '-ro' not in filepath:
        pass
    else:
        ext = filepath.split('-ro')[1]
        new_name = f"dataset_{i}{ext}"
        new_path = os.path.join(folder, new_name)
        os.rename(filepath, new_path)
        print(f"{filename} → {new_name}")
