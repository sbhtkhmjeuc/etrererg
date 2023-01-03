# imports
import requests
import json
from bs4 import BeautifulSoup

# Variables
URL = 'https://riskybiznews.substack.com/p/risky-biz-news-recent-okta-source'
r = requests.get(url = URL).text
soup = BeautifulSoup(r, 'html.parser')
print(soup)