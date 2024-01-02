#code was made using the tutorial here for email script:
#https://www.youtube.com/watch?v=d07QQVQ8M9g

#used the following tutorial for app password 2FA issue:
#https://www.youtube.com/watch?v=Y_u5KIeXiVI

#used the following tutorial for hiding credentials etc.:
#https://www.youtube.com/watch?v=YdgIWTYQ69A

import yagmail

from dotenv import load_dotenv
import os

load_dotenv()

SENDER_EMAIL_PWORD=os.getenv("SENDER_EMAIL_PWORD")
SENDER_EMAIL=os.getenv("SENDER_EMAIL")
RECEIVER_EMAIL=os.getenv("RECEIVER_EMAIL")

print('stored env variables')

print('reading env variables')

sender_password = f"{SENDER_EMAIL_PWORD}"
sender_email = f"{SENDER_EMAIL}"
receiver_email = f"{RECEIVER_EMAIL}"

print('code is starting')

print('creating email content')

body = 'this is a python email'
filename = ['testdoc.docx']

print('creating and sending email')
yag = yagmail.SMTP(sender_email, sender_password)
yag.send(
    to=receiver_email,
    subject='test mail',
    contents=body,
    attachments=filename
)

print('email sent')