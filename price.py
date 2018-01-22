import os
import threading
from datetime import datetime, timedelta
from time import sleep
from urllib import parse

import MySQLdb
import requests
from bs4 import BeautifulSoup

CLEARDB_DATABASE_URL = os.environ.get('CLEARDB_DATABASE_URL')
url = parse.urlparse(CLEARDB_DATABASE_URL)
db_info = {
    'NAME': url.path[1:],
    'USER': url.username,
    'PASSWORD': url.password,
    'HOST': url.hostname,
    'PORT': url.port if url.port else 3306,
}


class Price:
    def __init__(self):
        self._run()
        sleep(400)
        self.timer.cancel()

    def _get_price(self):
        base_url = 'https://www.coingecko.com/ja/%E7%9B%B8%E5%A0%B4%E3%83%81%E3%83%A3%E3%83%BC%E3%83%88/'

        self.btc = BeautifulSoup(requests.get(base_url + 'bitcoin' + '/usd').text,
                                 'lxml').find("div", class_="coin-value").span.text.replace("\n", "")

        self.zny = BeautifulSoup(requests.get(base_url + 'bitzeny' + '/usd').text,
                                 'lxml').find("div", class_="coin-value").span.text.replace("\n", "")

        self.bco = BeautifulSoup(requests.get(base_url + 'bridgecoin' + '/usd').text,
                                 'lxml').find("div", class_="coin-value").span.text.replace("\n", "")

        self.doge = BeautifulSoup(requests.get(base_url + 'dogecoin' + '/usd').text,
                                  'lxml').find("div", class_="coin-value").span.text.replace("\n", "")
        self.xp = BeautifulSoup(requests.get(base_url + 'xp' + '/usd').text,
                                'lxml').find("div", class_="coin-value").span.text.replace("\n", "")
        self.ytn = BeautifulSoup(requests.get(base_url + 'ytn' + '/usd').text,
                                 'lxml').find("div", class_="coin-value").span.text.replace("\n", "")

    def _update_price(self):
        con = MySQLdb.connect(user=db_info.get('USER'),
                              passwd=db_info.get('PASSWORD'),
                              host=db_info.get('HOST'),
                              db=db_info.get('NAME'))
        cur = con.cursor()
        update_sql = "update price set price='{price}' , update_date='{time}' where symbol='{symbol}';"
        now = (datetime.now() + timedelta(hours=9)
               ).strftime('%Y-%m-%d %H:%M:%S')
        cur.execute(update_sql.format(price=self.btc, time=now, symbol="btc",))
        cur.execute(update_sql.format(price=self.zny, time=now, symbol="zny",))
        cur.execute(update_sql.format(price=self.bco, time=now, symbol="bco",))
        cur.execute(update_sql.format(
            price=self.doge, time=now, symbol="doge",))
        cur.execute(update_sql.format(price=self.xp, time=now, symbol="xp",))
        cur.execute(update_sql.format(price=self.ytn, time=now, symbol="ytn",))
        con.commit()
        cur.close
        con.close

    def _run(self):
        self.timer = threading.Timer(150, self._run)
        self.timer.start()
        self._get_price()
        self._update_price()


def main():
    app = Price()


if __name__ == '__main__':
    main()
