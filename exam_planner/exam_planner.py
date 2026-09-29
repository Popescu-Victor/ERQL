import pandas
import os
import numpy as np


# Create a DataFrame to store exam information
df = pandas.DataFrame(columns=["Name", "Group", "Reading/UOE", "Listening", "Writing"])

# Convert the DataFrame to a CSV file
print("Enter filename: ")
filename = input()
df.to_csv(filename, index=False)