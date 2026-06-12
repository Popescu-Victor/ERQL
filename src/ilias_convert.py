import pandas as pd
from collections import defaultdict

# Converting raw csv files into a format that can be easily copy-pasted into ILIAS, which is the LMS we use. This is for the homework data, which is scraped from the LMS and then converted into a format that can be easily copy-pasted back into the LMS, so that teachers don't have to do it manually. The function takes a file path as input and returns a string that can be copy-pasted into ILIAS. The string contains the student username, the number of uncorrected homework, and the links to the uncorrected homework.


def convert_csv_to_ilias_format(filepath):

    df = pd.read_csv(filepath)
    hw_link = df.iloc[:, 3].tolist()
    student_username = df.iloc[:, 5].tolist()

    student_username = [i.replace("Test Passes for Participant: ", "") for i in student_username]
    hw_link = [i.replace(i, '''[xln url="'''+ i + '''"]Link[/xln]''') for i in hw_link]

    result = defaultdict(list)

    for k, v in zip(student_username, hw_link):
        result[k].append(v)

    output_final = ["Nume\tNumar Teme Necorectate\tLinkuri"]
    for k, v in result.items():
        output_final.append(f"{k} are {len(v)} teme necorectate: {' '.join(v)} ")
    return "\n".join(output_final)
