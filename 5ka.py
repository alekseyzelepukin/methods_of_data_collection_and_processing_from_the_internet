from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://5ka.ru/special_offers/')
pages = 0
while True:
    pages += 1
    try:

        #button = driver.find_element_by_class_name('special-offers__more-btn')
        button = WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'special-offers__more-btn'))
        )
        button.click()

    except:
        print(f'Всего {pages} страниц')
        break

goods = driver.find_elements_by_class_name('sale-card__footer')
for good in goods:
    try:
        print(good.find_element_by_class_name('sale-card__title').text)
        print(float(good
                    .find_element_by_class_name('sale-card__price--new')
                    .find_element_by_xpath('span[1]')
                    .text)/100)
    except:
        print('Сбор данных окончен')
