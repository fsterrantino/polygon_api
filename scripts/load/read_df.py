import pandas as pd
from datetime import datetime, timedelta

def read_df():
    path = './archives/'

    yesterday_date = datetime.now() - timedelta(days=1)
    formatted_date = yesterday_date.strftime('%Y.%m.%d')

    archive_name = 'stocks_bars - ' + formatted_date + '.csv'
    # archive_name = 'stocks_bars - 2023.12.15.csv'

    df = pd.read_csv(path + archive_name, index_col=False, sep=';')
    print('Archive to insert correctly read.')
    print(df.head())

    return df

