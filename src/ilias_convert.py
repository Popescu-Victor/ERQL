import pandas as pd
from collections import defaultdict

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
