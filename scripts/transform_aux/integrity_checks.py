import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timedelta

def where_or_and_condition(list, clause, column_to_query):
    string_list_elements = ', '.join(f"'{item}'" for item in list)
    query_condition = f"{clause} {column_to_query} IN ({string_list_elements})"
    return query_condition

def obtain_current_df_from_redshift(df_to_insert, engine):
    current_date_list = df_to_insert['datetime'].unique().tolist()
    current_stocks_list = df_to_insert['ticker'].unique().tolist()

    current_date_query_string = where_or_and_condition(current_date_list, 'WHERE', 'datetime')
    current_stocks_query_string = where_or_and_condition(current_stocks_list, 'AND', 'ticker')

    try:
        sql_query = f"SELECT * FROM stocks_data {current_date_query_string} {current_stocks_query_string}"
        current_df = pd.read_sql(sql_query, engine)
        print('Current table info accessed Ok.')
        return current_df

    except SQLAlchemyError as e:
        print("SQLAlchemy error:", e)

    except Exception as e:
        print("An error occurred:", e)

def obtain_df_to_insert_without_duplicates(current_df, df_to_insert):  
    df_to_insert['datetime'] = pd.to_datetime(df_to_insert['datetime'])
    print('Number of rows to insert:', df_to_insert.shape[0], '(before duplicates check)')

    compare_cols = ['ticker', 'datetime']
    common_rows = pd.merge(current_df, df_to_insert, on=compare_cols, how='inner')

    mask = ~((df_to_insert[compare_cols[0]].isin(common_rows[compare_cols[0]])) & (df_to_insert[compare_cols[1]].isin(common_rows[compare_cols[1]])))
    df_to_insert_unique = df_to_insert[mask]

    current_date = datetime.now()
    yesterday_date = current_date - timedelta(days=1)
    formatted_date = yesterday_date.strftime('%Y.%m.%d')

    archive_name = 'stocks_bars - unique rows - ' + formatted_date + '.csv'
    df_to_insert_unique.to_csv('/opt/archives/' + archive_name, index=False, sep=';')
    print('df_to_insert with unique values created.')

    if not common_rows.empty:
        archive_name = 'stocks_bars - duplicated rows - ' + formatted_date + '.csv'

        common_rows.to_csv('/opt/archives/' + archive_name, index=False, sep=';')
        print('Duplicates where identified. Number of rows:', common_rows.shape[0]) 
        print('Aux archive with duplicates generated.')
        
    else:
        print('There are not duplicated values.')

    print('Records to insert:', df_to_insert_unique.shape[0])
    return df_to_insert_unique

def avoid_inserting_duplicates(df_to_insert, engine):
    print('Starting duplicates check.')
    current_redshift_df = obtain_current_df_from_redshift(df_to_insert, engine)
    df_to_insert_unique = obtain_df_to_insert_without_duplicates(current_redshift_df, df_to_insert)
    print('Duplicates check finished.')
    return df_to_insert_unique




