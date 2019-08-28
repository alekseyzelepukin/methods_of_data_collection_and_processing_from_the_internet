from pprint import pprint
import csv
import pandas as pd
from requests import get
url = 'https://data.gov.ru/opendata/7710537160-drugsdestruction/data-20190826T2241-structure-20190826T2241.csv'
url2 = 'https://data.gov.ru/opendata/6163030330-ispolnenieoblbudgetpodrazdel/data-20190826T1553-structure-20190826T1553.csv'
# data = get(url)
data_frame = pd.read_csv(url,sep=';')
result = data_frame[data_frame["'status'"] == "'недоброкачественное ЛС'"]
print(result)

# f = open('data.csv','wb')
# f.write(data.content)
# f.close()



# with open('data.csv','r', encoding='UTF-8') as f:
#     reader = csv.DictReader(f, delimiter=';')
#     field_names = reader.fieldnames
#
#     for row in reader:
#         print(row["'owner'"], row["'manufacturer'"], row["'status'"])
