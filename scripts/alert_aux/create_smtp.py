import smtplib
from scripts.common_aux.config_read import config_read
from dotenv import load_dotenv
import os

def create_smtp():
        print('Connecting SMTP server.')
        x=smtplib.SMTP('smtp.gmail.com', 587)
        x.starttls()

        config = config_read()
        email_sender = config['ALERTS_EMAIL']['sender']

        load_dotenv(dotenv_path='./.env')
        EMAIL_APP_KEY = os.getenv('EMAIL_APP_KEY')

        x.login(email_sender, EMAIL_APP_KEY)

        return x, email_sender

