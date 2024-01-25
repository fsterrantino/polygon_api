from scripts.alert_aux.create_smtp import create_smtp
from scripts.common_aux.config_read import config_read
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(df):
    print('Sending email.')

    smtp_instance, sender = create_smtp()

    subject = 'Rule - Close_price % Increase/Descrease - Alerted stocks'
    
    message = MIMEMultipart()
    message['Subject'] = subject

    html_content = f"""
    <html>
        <body>
            <p>Alerted stocks:</p>
            {df.to_html()}
        </body>
    </html>
    """

    message.attach(MIMEText(html_content, 'html'))

    config = config_read()
    destinatary = config['ALERTS_EMAIL']['destinatary']

    smtp_instance.sendmail(sender, destinatary, message.as_string())
    smtp_instance.quit()

    print('Email sent.')
