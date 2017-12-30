import os
import smtplib
import time
from threading import Timer

import requests

MAILGUN_API_KEY=os.environ.get('MAILGUN_API_KEY')
MAILGUN_DOMAIN = os.environ.get('MAILGUN_DOMAIN')
MAILGUN_PUBLIC_KEY = os.environ.get('MAILGUN_PUBLIC_KEY')
TO_ADDRESS = os.environ.get('TO_ADDRESS')
FROM_ADDRESS = os.environ.get('MAILGUN_SMTP_LOGIN')

class Email:
    def send_mail(self,to_address, from_address, subject, plaintext):
        r = requests.post("https://api.mailgun.net/v3/%s/messages" % MAILGUN_DOMAIN,
                                auth=("api", MAILGUN_API_KEY),
                                data={
                "from": from_address,
                "to": to_address,
                "subject": subject,
                "text": plaintext,
        })
        return r


def run():
        # t = Timer(3600, run)
        # t.start()
        a = Email()
        res = a.send_mail(TO_ADDRESS, FROM_ADDRESS, "testEmail", "can you receive?")
        print(res.status_code)

if __name__ == '__main__':
        run()
