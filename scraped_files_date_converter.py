import pandas as pd
from dateutil import parser
import os

test_file = r""

df = pd.read_excel(test_file)
dates = []


print(test_file)

for d in df.iloc[:, -1]:
    if d == "Yesterday":
        dates.append("2025-11-04")
    else:
        parsed = parser.parse(d)
        dates.append(parsed.strftime("%Y-%m-%d"))

for d in dates:
    print(parser.parse('2025-11-05') - parser.parse(d))
