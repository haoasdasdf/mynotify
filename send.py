import os
import sendgrid
import time
from threading import Timer
from sendgrid.helpers.mail import *

import requests

SENDGRID_API = os.environ.get('SENDGRID_API')
SENDGRID_USERNAME = os.environ.get('SENDGRID_USERNAME')
SENDGRID_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
TO_ADDRESS = os.environ.get('TO_ADDRESS')
FROM_ADDRESS = os.environ.get('SENDGRID_USERNAME')
MAIL_SUBJECT = os.environ.get('MAIL_SUBJECT')
MAIL_CONTENT = os.environ.get('MAIL_CONTENT')


class SendEmail:
    def send_mail(self, subject, plaintext):
        sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API)
        from_email = Email(FROM_ADDRESS)
        to_email = Email(TO_ADDRESS)
        content = Content("text/plain", plaintext)
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        return (response)


def run():
    a = SendEmail()
    r = a.send_mail(MAIL_SUBJECT, MAIL_CONTENT)
    print(r.status_code)
    print(r.body)
    print(r.headers)


if __name__ == '__main__':
    run()
