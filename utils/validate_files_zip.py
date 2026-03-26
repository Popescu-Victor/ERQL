# Returnes list of files in zip without duplicates or irelevant ones.
import zipfile

def validate_files(filepath):
    list_of_clean_reports = []
    
    with zipfile.ZipFile(filepath, "r") as z:
        files = z.namelist()
        for i, filename in enumerate(files, start=1):
            if '-ro-' not in filename:
                pass
            else:
                ext = filename.split('-ro-')[1]
                if len(ext) == 15:
                    list_of_clean_reports.append(filename)
                else:
                    pass
                    
    return list_of_clean_reports


print(validate_files(r"C:\Users\popescu.victor\Desktop\Colab.zip"))


