import os
import sendgrid
import smtplib
import time
from threading import Timer
from sendgrid.helpers.mail import *

import requests

SENDGRID_API = os.environ.get('SENDGRID_API')
SENDGRID_USERNAME = os.environ.get('SENDGRID_USERNAME')
SENDGRID_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
TO_ADDRESS = os.environ.get('TO_ADDRESS')
FROM_ADDRESS = os.environ.get('SENDGRID_USERNAME')


class Email:
    def send_mail(self, to_address, from_address, subject, plaintext):
        sg = sendgrid.SendGridAPIClient(
            apikey=SENDGRID_API)
        from_email = Email(FROM_ADDRESS)
        subject = "In Stock"
        to_email = Email(TO_ADDRESS)
        content = Content("text/plain", "Please check items")
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)


def run():
    # t = Timer(3600, run)
    # t.start()
    a = Email()
    res = a.send_mail(TO_ADDRESS, FROM_ADDRESS,
                      "testEmail", "can you receive?")
    print(res.status_code)


if __name__ == '__main__':
    run()
