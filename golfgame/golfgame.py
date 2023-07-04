import os
from data.fetch import fetch
from data.process import process

FORCE_UPDATE = False
URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSQBUyHYW958Nrej2ZAkz3r0G-vqWTEeKPXs2abbHHBfCOvImEf-SYTzLC31qTZl1djGToNjstHItjV/pub?gid=757942375&single=true&output=csv'

if not os.path.isfile('data.csv') or FORCE_UPDATE:
    fetch(URL)

data = process()
print(data)