import requests
from bs4 import BeautifulSoup
from datetime import *
from urllib import parse
import MySQLdb
import os

# CLEARDB_DATABASE_URL = os.environ.get('CLEARDB_DATABASE_URL')
CLEARDB_DATABASE_URL = 'mysql://b8f52406326a20:c044b4d5@us-cdbr-iron-east-05.cleardb.net/heroku_d72f255429a03f3?reconnect=true'
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
        self._get_price()
        self._update_price()

    def _get_price(self):
        base_url = 'https://www.coingecko.com/ja/%E7%9B%B8%E5%A0%B4%E3%83%81%E3%83%A3%E3%83%BC%E3%83%88/'

        self.btc = BeautifulSoup(requests.get(base_url + 'bitcoin' + '/usd').text,
                                 'lxml').find("div", class_="coin-value").span.text

        self.zny = BeautifulSoup(requests.get(base_url + 'bitzeny' + '/usd').text,
                                 'lxml').find("div", class_="coin-value").span.text

        self.bco = BeautifulSoup(requests.get(base_url + 'bridgecoin' + '/usd').text,
                                 'lxml').find("div", class_="coin-value").span.text

        self.doge = BeautifulSoup(requests.get(base_url + 'dogecoin' + '/usd').text,
                                  'lxml').find("div", class_="coin-value").span.text

        self.xp = BeautifulSoup(requests.get(base_url + 'xp' + '/usd').text,
                                'lxml').find("div", class_="coin-value").span.text

    def _update_price(self):
        con = MySQLdb.connect(user=db_info.get('USER'),
                              passwd=db_info.get('PASSWORD'),
                              host=db_info.get('HOST'),
                              db=db_info.get('NAME'))
        cur = con.cursor()
        update_sql = "update price set price=%s and update_date=%s where symbol=%s;"
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        cur.execute(update_sql, (self.btc, now, 'btc'))
        cur.execute(update_sql, (self.zny, now, 'zny'))
        cur.execute(update_sql, (self.bco, now, 'bco'))
        cur.execute(update_sql, (self.doge, now, 'doge'))
        cur.execute(update_sql, (self.xp, now, 'xp'))

        cur.close
        con.close

    def _watch(self):
        con = MySQLdb.connect(user=db_info.get('USER'),
                              passwd=db_info.get('PASSWORD'),
                              host=db_info.get('HOST'),
                              db=db_info.get('NAME'))
        cur = con.cursor()
        sql = "select * from price"
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close
        con.close
        info = []
        for row in rows:
            one = {}
            one.update({
                'name': row[1],
                'price': row[3],
                'update_time': row[4]
            })
            info.append(one)
        print(info)


def main():
    app = Price()


if __name__ == '__main__':
    main()
