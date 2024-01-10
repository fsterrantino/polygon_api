import pandas as pd

def read_df(df_type, date):
    print('Check formatted yesterday date from airflow:')
    path = '/opt/archives/'

    date = date.replace('-', '.')

    if df_type == 'unique':
        archive_name = 'stocks_bars - unique rows - ' + date + '.csv'
    elif df_type == 'normal':
        archive_name = 'stocks_bars - ' + date + '.csv'
 
    df = pd.read_csv(path + archive_name, index_col=False, sep=';')
    print('Archive to insert correctly read.')
    print(df.head())

    return df

