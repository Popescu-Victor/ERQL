# Takes in multiple excel files and counts how many times a student's name appears in the list of ungraded homework assignments.

import os
import pandas as pd


hashmap = {}


for x in list_of_clean_reports: # list_of_clean_reports is in "validate_files.py"
    df = pd.read_excel(x)
    for col in df.columns:
            if df[col].astype(str).str.contains("Test Passes for Participant:", case=False, na=False).any():
                user_col = df.columns.get_loc(col)
                for x in df.iloc[:,user_col]:
                    if len(x.split("Participant: ")) > 1:
                        total_hw_entries += 1
                        if x in hashmap:
                            hashmap[x] += 1
                        else:
                            hashmap[x] = 1
    
for x, y in hashmap.items():
    print(x,y)
print("Total homework entries for this course: " + str(total_hw_entries))
