from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import re
from datetime import datetime

# url = 'https://www.yes24.com/Product/Goods/122120495'
# url = 'https://www.yes24.com/Product/Goods/117014613'
url = 'https://www.yes24.com/Product/Goods/124472862'

browser = webdriver.Chrome()
browser.get(url)
# .find_element(By.CLASS_NAME, 'gd_ratingArea').
# is_ratingOk = browser.find_elements(By.CLASS_NAME, 'gd_rating')
# if is_ratingOk:
#     print("Element found.")
# else:
#     print("Element not found.")

# is_reviewOk = browser.find_elements(By.CSS_SELECTOR, 'span.gd_reviewCount em.txC_blue')
# if is_reviewOk:
#     print("Element found.")
# else:
#     print("Element not found.")

is_full_textOk = browser.find_elements(By.CSS_SELECTOR, 'span.gd_best dd')
if is_full_textOk:
    full_text = browser.find_element(By.CLASS_NAME, 'gd_best').find_element(By.TAG_NAME, 'dd').text
    parts = full_text.split(" | ") 
    ranking_part = parts[0]
    ranking = ''.join(filter(str.isdigit, ranking_part)) # 숫자만 추출
    ranking_weeks_part = parts[1]
    ranking_weeks = ''.join(filter(str.isdigit, ranking_weeks_part.split()[-1]))
else:
    ranking = 0
    ranking_weeks = 0

print(ranking, ranking_weeks)

# sales = browser.find_element(By.CLASS_NAME, 'gd_sellNum').text.split(" ")[2]
# sales = int(sales.replace(",", ""))
# price = browser.find_element(By.CLASS_NAME, 'yes_m').text[:-1]
# price = int(price.replace(",", ""))
# print(rating, review, sales, price)