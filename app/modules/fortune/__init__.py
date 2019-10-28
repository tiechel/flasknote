import requests
import datetime
import json
from app.models import Fortune

# http://api.jugemkey.jp/api/horoscope/free/year/month/day
endpoint = 'http://api.jugemkey.jp/api/horoscope/free/'


def get_fortune(date=datetime.datetime.today()):
    date_str = date.strftime(endpoint + '{}/{}/{}'.format())
    response = requests.get(url=endpoint + '{}/{}/{}'.format())
