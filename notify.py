import os

import requests
import sendgrid
from bs4 import BeautifulSoup
from sendgrid.helpers.mail import *

TARGET_URL = os.environ.get('TARGET_URL')
SENDGRID_API = os.environ.get('SENDGRID_API')
SENDGRID_USERNAME = os.environ.get('SENDGRID_USERNAME')
SENDGRID_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
TO_ADDRESS = os.environ.get('TO_ADDRESS')
FROM_ADDRESS = os.environ.get('SENDGRID_USERNAME')
MAIL_SUBJECT = os.environ.get('MAIL_SUBJECT')
MAIL_CONTENT = os.environ.get('MAIL_CONTENT')


class NotifyApp:

    def __init__(self):
        self.search = self._search()
        print(self.search)
        if(self.search is True):
            self._sendMail()

    def _search(self):
        r = requests.get(TARGET_URL)
        soup = BeautifulSoup(r.text, 'lxml')
        sub = soup.body.find_all('a', class_='submit')
        if(sub):
            return True
        return False

    def _sendMail(self):
        sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API)
        from_email = Email(FROM_ADDRESS)
        to_email = Email(TO_ADDRESS)
        content = Content("text/plain", MAIL_CONTENT)
        mail = Mail(from_email, MAIL_SUBJECT,
                    to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        return (response)


def main():
    app = NotifyApp()

if __name__ == '__main__':
    main()
