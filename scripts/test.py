from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

def greetings():
    print('Hola')

    load_dotenv(dotenv_path='./.env')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    print('Database pw:', DATABASE_PASSWORD)