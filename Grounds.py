import requests
from pprint import pprint
from pymongo import MongoClient
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

page_link='https://www.svoya-zemlya.ru'
client = MongoClient('mongodb://127.0.0.1:27017')
db = client['grounds']
groundsdb = db.grounds


def get_html(url):
    try:
        response = requests.get(url, headers = {'User-Agent':UserAgent().chrome})
    except:
        raise exception('Ошибка подключения')
    # for k,v in response.request.headers.items():
    #     print(k + " : " + v)
    with open ('index.html','wb') as f:
        f.write(response.content)
    soup = BeautifulSoup(response.text,'html.parser')
    return soup

def get_links(soup):
    plants = soup.find_all('div',{'class':'item'})
    plants_links = [item.div.a.attrs['href'] for item in plants]
    return plants_links
    # for item in plants_links:
    #     print(item)

link_part2 = '/catalog/dachi/'
soup = get_html(page_link+link_part2)
links = get_links(soup)
for link in links:
    info_html = get_html(page_link+link)
    main = info_html.find('div',attrs={'id':'forPrint'})  #Опорный элемент
    name = main.h1.span.text
    min_price = main.find('div',{'class':'pirce_pos'}).text
    comfort_obj = main.find('ul',{'class':'ct_comynik'}).findChildren()
    comfort_list = [item.text for item in comfort_obj]
    try:
        price = main.find(text = 'Прайс-лист').findParent()
    except:
        print(f'У {name} нет прайса')
        continue
    price_link = price['href']
    try:
        plants_list_html = get_html(page_link+price_link)
    except:
        pprint(f'Ошибка доступа к данным у {name}')
        continue


    table = plants_list_html.find('table',{'class':'comp_table'})
    table_data = table.tbody.find_all('tr')
    plant_data=[]
    for row in table_data:
        plant_info = row.findChildren(limit = 5)
        plant_map = plant_info[0].text
        plant_num = plant_info[1].text
        plant_square = plant_info[2].text
        plant_state = plant_info[3].text
        plant_price = plant_info[4].text
        plant_data.append({
            'map': plant_map,
            'num':plant_num,
            'square': float(plant_square),
            'state': plant_state,
            'price':float(plant_price.replace(' ','')[:-4])
        })
    item = {
        'name':name,
        'min_price':min_price,
        'comfort':comfort_list,
        'plant_data':plant_data
    }

    myquery={'name':item['name']}

    if groundsdb.count_documents(myquery)>0:
        newvalues = {"$set":item}
        groundsdb.update_one(myquery,newvalues)
        print(f"Документ {item['name']} обновлен в базе")
    else:
        groundsdb.insert_one(item)
        print(f"Документ {item['name']} добавлен в базу")


