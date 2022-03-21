from bs4 import BeautifulSoup
import requests, re

r = requests.get('http://webscraper.io/test-sites/e-commerce/allinone/phones').content
soup = BeautifulSoup(r, "lxml")
p = re.compile('[A-Za-z0-9_%.-]+@[A-z0-9_%.-]+\.[A-z0-9]{2,}')
span = soup.find("<span class=")
price = span
print(price)
print(type(soup)) 
print(soup.prettify()[:100])
for link in soup.find_all('a'): print(link.get('href'))