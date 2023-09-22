from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, ssl
from twilio.rest import Client


def email_sending(error):
    """Emails credentials for login"""
    sender_email = "Sender_Email_address"
    receiver_email = "Receiver_Email_address"
    password = 'Sender_Email_Passwd'

    message = MIMEMultipart("alternative")
    message["Subject"] = "There is a code error in the Archive system"
    message["From"] = sender_email
    message["To"] = receiver_email

    # The text variable is the message
    text = f'An error just encountered:\n   "{error}"'

    part1 = MIMEText(text, "plain")

    message.attach(part1)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
        server.close()

    # print("Mail is sent")


def whatsapp_alert():
    """Need to use Twilio for the cloud part and the Auth code: https://www.twilio.com/"""
    account_sid = 'Token_here'
    auth_token = 'Token_here'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp: SenderNum_here',
        body='There is an error at the archive system!',
        to='whatsapp: ReceiverNum_here'
    )
