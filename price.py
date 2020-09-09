import os
import threading
from datetime import datetime, timedelta
from time import sleep
from urllib import parse

import pymysql.cursors
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

coins = {
	# { 'name': 'symbol' }
	'bitcoin': 'btc',
	'bitzeny': 'zny',
	'bridgecoin': 'bco',
	'dogecoin': 'doge',
	'xp': 'xp',
	'yenten': 'ytn',
		'monero': 'xmr'
}

class Price:
	def __init__(self):
		self._run()
		# sleep(400)
		# self.timer.cancel()

	def _get_price(self):
		self.base_url = 'https://www.coingecko.com/en/price_charts/'
		for name, symbol in coins.items() :
			url = self.base_url + name + '/usd'
			print (url)
			price = BeautifulSoup(requests.get(url).text,
			'lxml').findAll("div", class_="text-3xl")[0].span.text

			print(price)
			self._update_price(price, symbol)

	def connectDB(self):
		self.con = pymysql.connect(user=db_info.get('USER'),
			passwd=db_info.get('PASSWORD'),
			host=db_info.get('HOST'),
			db=db_info.get('NAME'))
		self.cur = self.con.cursor()

	def _update_price(self, price, symbol):
		update_sql = ("update price set price='{price}' , update_date='{time}' where symbol='{symbol}';")
		self.cur.execute(update_sql.format(price=price, time=self.now, symbol=symbol,))

		self.con.commit()

	def closeDB(self):
		self.cur.close
		self.con.close

	def _run(self):
		# self.timer = threading.Timer(150, self._run)
		# self._run
		# self.timer.start()
		self.now = (datetime.now() + timedelta(hours=9)).strftime('%Y-%m-%d %H:%M:%S')
		self.connectDB()
		self._get_price()
		self.closeDB()
		# self._update_price()

def main():
	app = Price()


if __name__ == '__main__':
	main()
