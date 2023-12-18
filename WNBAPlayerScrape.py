import unicodedata
import bs4
import json
from bs4 import BeautifulSoup
import pandas as pd
import re
import requests

playersurl = ('https://www.wnba.com/players')

playerrequest = requests.get(playersurl)

soup = BeautifulSoup(playerrequest.content, 'html.parser')
scriptTag = soup.find(id="__NEXT_DATA__")
a = scriptTag.string
obj = json.loads(json.loads(json.dumps(a)))
# print(json.dumps(obj, indent=2))
props = obj['props']
headers = props['siteHeaderOptions']
teams = headers['teams']

pageData = props['pageProps']
players = pageData["allPlayersData"]

print(players)
# tid, ta, tn, tc
for i in teams:
    fullName = i['tc'] + ' ' + i['tn']
    arr = [i['tid'],i['ta'], i['tn'], i['tc'], fullName, i['sta']]
    print(arr)


