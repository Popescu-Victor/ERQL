import pandas as pd


def main(col_no: int):
    col_names = []
    for i in range(int(col_no)):
        col_names.append(input(">>  "))
    created_df = pd.DataFrame(columns=col_names)
    print(created_df)
    return created_df



def add_data(df):
    new_row = []
    for i in range(df.shape[1]):
        input_data = input(">>> ")
        new_row.append(input_data)
    input_data_series = pd.Series(new_row)
    new_df = pd.concat([df, input_data_series], ignore_index=True)
    return new_df


how_many_col = input("How many columns? ")
dataframe1 = main(how_many_col)
add_data(dataframe1)


print(dataframe1.head())