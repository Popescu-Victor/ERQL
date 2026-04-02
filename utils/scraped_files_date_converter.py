import pandas as pd
from dateutil import parser
import os

test_file = r"" #Add test file path here

df = pd.read_excel(test_file)
dates = []


print(test_file)

for d in df.iloc[:, -1]:
    if d == "Yesterday":
        dates.append("2025-11-04") # IMPORTANT: This only works for files uploaded on this specific date. Make it so that the program takes the date from the file's name! 
    else:
        parsed = parser.parse(d)
        dates.append(parsed.strftime("%Y-%m-%d"))

for d in dates:
    print(parser.parse('2025-11-05') - parser.parse(d))

def find_column(df, text): # This find the column with the users in each excel file in a folder.
    for col in df.columns:
        if df[col].astype(str).str.contains(text, case=False, na=False).any():
            return df.columns.get_loc(col)
    return None


def user_column_display(): # This prints out where to find the user column in each excel table.
    for i, filename in enumerate(files, start=1):
        filepath = os.path.join(folder, filename)
        if '-ro' not in filepath:
            pass
        else:
            df = pd.read_excel(filepath)
            if find_column(df, "Test Passes for Participant:") != None:
                print(filename + " has col: " + str(find_column(df, "Test Passes for Participant:")))


