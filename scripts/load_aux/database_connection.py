import psycopg2
import configparser
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from common_aux.config_read import config_read

load_dotenv(dotenv_path='./.env')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

config = config_read()

dbname = config.get('DATABASE_CONNECTION', 'dbname')
host = config.get('DATABASE_CONNECTION', 'host')
port = config.get('DATABASE_CONNECTION', 'port')
user = config.get('DATABASE_CONNECTION', 'user')
password = DATABASE_PASSWORD

def connect_database():

    try:
        conn = psycopg2.connect(
            dbname = dbname,
            host = host,
            port = port,
            user = user,
            password = password
        )

        cursor = conn.cursor()

        print('DB connection established.')
        return conn, cursor

    except psycopg2.Error as e:
        print("Error connecting to Redshift:", e)


def create_sqlAlchemy_engine():
    conn_string = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
    engine = create_engine(conn_string)
    return engine


def disconnect_database(conn, cursor):
    cursor.close()
    conn.close()
    print('DB disconnected.')