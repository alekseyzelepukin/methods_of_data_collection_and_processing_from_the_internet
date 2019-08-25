from zeep import Client
from pprint import pprint
url='https://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx?WSDL'
client = Client(url)
money = client.service.GetCursOnDate('2019-08-21')
list_money = money._value_1._value_1
for item in list_money:
    for v in item.values():
        if v.VchCode == 'USD':
            print(item['ValuteCursOnDate']['Vcurs'])


