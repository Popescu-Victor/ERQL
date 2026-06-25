import pandas as pd


def main(col_no: int):
    col_names = []
    for i in range(col_no):
        col_names.append(input(">>  "))
    created_df = pd.DataFrame(columns=col_names)
    print(created_df)

main(3)