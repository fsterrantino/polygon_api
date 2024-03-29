import pandas as pd
from sqlalchemy.exc import SQLAlchemyError

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

def obtain_df_to_insert_without_duplicates(current_df, df_to_insert, yesterday_date):  
    df_to_insert['datetime'] = pd.to_datetime(df_to_insert['datetime'])
    print('Number of rows to insert:', df_to_insert.shape[0], '(before duplicates check)')

    # The script checks if the combination ticker, datetime, it's already inserted in Postgre.
    compare_cols = ['ticker', 'datetime']
    common_rows = pd.merge(current_df, df_to_insert, on=compare_cols, how='inner')

    # The mask flag each row if the ticker is in common_rows, and if datetime is in common rows. If both are true for a row, it's excluded as 'False' to be filtered in the df_to_insert_unique.
    mask = ~((df_to_insert[compare_cols[0]].isin(common_rows[compare_cols[0]])) & (df_to_insert[compare_cols[1]].isin(common_rows[compare_cols[1]])))
    df_to_insert_unique = df_to_insert[mask]

    formatted_yesterday_date = yesterday_date.replace('-', '.')

    archive_name = 'stocks_bars - unique rows - ' + formatted_yesterday_date + '.csv'
    df_to_insert_unique.to_csv('/opt/archives/' + archive_name, index=False, sep=';')
    print('df_to_insert with unique values created.')

    if not common_rows.empty:
        archive_name = 'stocks_bars - duplicated rows - ' + formatted_yesterday_date + '.csv'

        common_rows.to_csv('/opt/archives/' + archive_name, index=False, sep=';')
        print('Duplicates where identified. Number of rows:', common_rows.shape[0]) 
        print('Aux archive with duplicates generated.')
        
    else:
        print('There are not duplicated values.')

    print('Records to insert:', df_to_insert_unique.shape[0])
    return df_to_insert_unique

def avoid_inserting_duplicates(df_to_insert, engine, formatted_yesterday_date):
    print('Starting duplicates check.')
    current_redshift_df = obtain_current_df_from_redshift(df_to_insert, engine)
    df_to_insert_unique = obtain_df_to_insert_without_duplicates(current_redshift_df, df_to_insert, formatted_yesterday_date)
    print('Duplicates check finished.')
    return df_to_insert_unique




