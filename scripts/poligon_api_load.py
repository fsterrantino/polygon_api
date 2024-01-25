from scripts.load_aux.read_df import read_df
from scripts.load_aux.database_connection import connect_database, disconnect_database, create_sqlAlchemy_engine
from scripts.load_aux.insert_df_into_db import insert_df_into_db
from scripts.extract_aux.obtain_yesterday_date import obtain_yesterday_date

def load_data(**kwargs):
    execution_date = kwargs.get('execution_date')
    formatted_yesterday_date = obtain_yesterday_date(execution_date)

    df_to_insert = read_df('unique', formatted_yesterday_date)
    df_to_insert['load_date'] = execution_date.strftime('%Y-%m-%d')

    connection, cursor = connect_database()
    sqlAlchemy_engine = create_sqlAlchemy_engine()

    insert_df_into_db(df_to_insert, sqlAlchemy_engine)
        
    disconnect_database(connection, cursor)