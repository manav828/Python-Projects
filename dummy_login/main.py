# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# import time

# from selenium.webdriver.common.by import By
#
# chrome_driver_path = 'D:\Manav\Software\chromedriver_win32'
# service = Service(chrome_driver_path)
#
# driver = webdriver.Chrome(service=service)
# # driver.get('https://practicetestautomation.com/practice-test-login/')
# driver.get('https://orteil.dashnet.org/experiments/cookie/')
#
# # search_user = driver.find_element('name','username')
# # search_pass = driver.find_element('name','password')
# submit_btn = driver.find_element('id' , 'cookie')
# #
# # search_user.send_keys('student')
# # search_pass.send_keys('Password123')
#
#
#
# time.sleep(500)
# driver.quit()


from bs4 import BeautifulSoup
import requests

web_page = 'https://www.amazon.in/s?k=hades+phone+bluetooth&sprefix=had%2Caps%2C658&ref=nb_sb_ss_ts-doa-p_2_3'
# driver.get(web_page)

res = requests.get(web_page)
web_text = res.text

soup = BeautifulSoup(web_text, 'html.parser')

img_link = soup.find_all('img', class_='s-image')
heading_text = soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')

item_data = []

for link, heading in zip(img_link, heading_text):
    # print(link.get('src'))
    item_data.append({
        'link': link.get('src'),
        'heading': heading.getText()
    })

print(item_data)

# for link in img_link:
#     print(link.get('src'))
