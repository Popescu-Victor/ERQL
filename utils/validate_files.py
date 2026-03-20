import os

folder = r""

files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

list_of_clean_reports = []


for i, filename in enumerate(files, start=1):
    filepath = os.path.join(folder, filename)
    if '-ro' not in filepath: # The scraper extension that I'm using returns files in the following format [site name] + [site extension] + [date]. The '-ro-' split here is to separate the date from the other parts of the file name.
        pass
    else:
        ext = filepath.split('-ro-')[1]
        if len(ext) == 15:
            list_of_clean_reports.append(filepath)
        else:
            pass

for x in list_of_clean_reports:
    print(x)
