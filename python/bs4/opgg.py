import requests as req
from bs4 import BeautifulSoup

res = req.get('https://tw.op.gg/')
print(res.text)