import pandas as pd


def credit_data_reader():

    # fetch data from csv file
    df = pd.read_csv('./data/credit_data_updated.csv', delimiter=';')

    # keep only the columns needed
    df = df[['name', 'bloomberg', 'date', 'last_price', 'yield']]

    # replace ',' with '.' and 'na' with 'NaN' in all columns
    df = df.stack().str.replace(',', '.').unstack()
    df = df.stack().str.replace('na', 'NaN').unstack()

    # specify dataypes in each column
    df = df.astype(
        {
            'name': 'string',
            'bloomberg': 'string',
            'date': 'datetime64',
            'last_price': 'float',
            'yield': 'float'
        }
    )

    # reverse order of dataset
    df = df.loc[::-1]

    # reset the indexation
    df.reset_index(inplace=True, drop=True)

    return df
