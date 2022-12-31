# imports
import requests
import json
from bs4 import BeautifulSoup

# Variables
URL = 'https://riskybiznews.substack.com/p/risky-biz-news-recent-okta-source'


r = requests.get(url = URL)
data = r.text
S = BeautifulSoup(data, 'lxml')
print(S.prettify())


# with open("sample.txt", "w") as file:
#     file.write(str(S.encode("utf-8")))