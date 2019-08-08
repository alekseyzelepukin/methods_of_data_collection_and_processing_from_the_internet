from pprint import pprint
import requests
import json
service = 'http://min-prices.aviasales.ru/calendar_preload?'
fromCity = 'MOW'
toCity = 'LED'
link = f'{service}origin={fromCity}&destination={toCity}&one_way=true'
req = requests.get(link)
data = json.loads(req.text)
for i in data['best_prices']:
    print(i['value'],i['depart_date'],i['return_date'],i['gate'])
