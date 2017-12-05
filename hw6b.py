import ssl
import re
import operator
from urllib.request import urlopen
from bs4 import BeautifulSoup

#------------------------------------------------------

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#------------------------------------------------------

url = input('Enter URL: ')
count = int(input('Enter Count: '))
position = int(input('Enter Position: '))
final = []

for item in range(count):
	html = urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	url = soup.find_all('a')[position - 1].get('href')
	final.append(url)
	print ('Retrieving: ', url)
