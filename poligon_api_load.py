from scripts.load.read_df import read_df
from scripts.load.database_connection import connect_database, disconnect_database, create_sqlAlchemy_engine
from scripts.load.insert_df_into_db import insert_df_into_db
from scripts.load.integrity_checks import avoid_inserting_duplicates

df_to_insert = read_df()
connection, cursor = connect_database()
sqlAlchemy_engine = create_sqlAlchemy_engine()
df_to_insert_unique = avoid_inserting_duplicates(df_to_insert, sqlAlchemy_engine)

if not df_to_insert_unique.empty:
    insert_df_into_db(df_to_insert_unique, sqlAlchemy_engine)
    
disconnect_database(connection, cursor)