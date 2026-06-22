import pandas as pd


user_input = input(">  ")
if not isinstance(user_input, str) or ">" not in user_input:
    print("Invalid input format.")


df = pd.DataFrame([user_input.split(">")])
print(df)