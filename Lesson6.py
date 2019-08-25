from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get('https://geekbrains.ru/login')
assert "GeekBrains" in driver.title
elem = driver.find_element_by_id("user_email")
elem.send_keys('study.ai_172@mail.ru')
elem = driver.find_element_by_id("user_password")
elem.send_keys('Password172')
elem.send_keys(Keys.RETURN)
assert "Главная | GeekBrains" in driver.title

profile = driver.find_element_by_class_name('avatar')
driver.get(profile.get_attribute('href'))

edit_profile = driver.find_element_by_class_name('text-sm')
driver.get(edit_profile.get_attribute('href'))

gender = driver.find_element_by_name('user[gender]')
#options = gender.find_elements_by_tag_name('option')

# for option in options:
#     if option.text == 'Женский':
#         option.click()
select = Select(gender)
select.select_by_value('2')

gender.submit()
driver.back()


driver.quit()
