from scripts.load_aux.read_df import read_df
from scripts.load_aux.database_connection import connect_database, disconnect_database, create_sqlAlchemy_engine
from scripts.transform_aux.integrity_checks import avoid_inserting_duplicates
from scripts.extract_aux.obtain_yesterday_date import obtain_yesterday_date

def transform_data(**kwargs):
    execution_date = kwargs.get('execution_date')
    formatted_yesterday_date = obtain_yesterday_date(execution_date)

    df_to_insert = read_df('normal', formatted_yesterday_date)
    connection, cursor = connect_database()
    sqlAlchemy_engine = create_sqlAlchemy_engine()
    df_to_insert_unique = avoid_inserting_duplicates(df_to_insert, sqlAlchemy_engine, formatted_yesterday_date)

    if df_to_insert_unique.empty:
        raise(f'Duplicates where found, please check if the datetime being requested had been already loaded into the DB.')
        
    disconnect_database(connection, cursor)