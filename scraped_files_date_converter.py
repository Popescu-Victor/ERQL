import pandas as pd
from dateutil import parser


test_file = r"path\file.xlsx"
dates = ['03. Nov 2025', '30. Oct 2025', '2025-11-05']

print(test_file)
for d in dates:
    parsed = parser.parse(d)
    print(parsed.strftime("%Y-%m-%d"))
