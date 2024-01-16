from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time
import pymysql
import re
from datetime import datetime

header_user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

options_ = Options()
options_.add_argument(f'user-agent={header_user}')
service = Service(ChromeDriverManager().install())

# browser = webdriver.Chrome(service=service, options=options_)
browser = webdriver.Chrome()

links = []
for i in range(1, 4):
    print('*' * 10, f'현재 {i}페이지 수집중입니다.', '*' * 10)
    url = f'https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001&pageNumber={i}&pageSize=24'
    browser.get(url)
    
    # data = browser.find_element(By.CLASS_NAME, 'gd_name').get_attribute('href')
    # 상세페이지 링크 데이터 수집 전부 수집
    datas = browser.find_elements(By.CLASS_NAME, 'gd_name')
    for i in datas:
        links.append(i.get_attribute('href'))
        
    time.sleep(3)
    
# 데이터 베이스 연동후 -> 수집한 데이터를 db 에 저장 (csv)
    
conn = pymysql.connect(
    # host='127.0.0.1',
    host='localhost',
    user='root',
    password='root',
    db='yes24',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with conn.cursor() as cursor:
    for link in links:
        browser.get(link)

        title = browser.find_element(By.CLASS_NAME, 'gd_name').text
        author = browser.find_element(By.CLASS_NAME, 'gd_auth').text
        publisher = browser.find_element(By.CLASS_NAME, 'gd_pub').text
        publishing = browser.find_element(By.CLASS_NAME, 'gd_date').text
        match = re.search(r'(\d+)년 (\d+)월 (\d+)일', publishing)
        if match:
            year, month, date = map(str, match.group().split())
            date_obj = datetime(int(year[:-1]), int(month[:-1]), int(date[:-1]))
            publishing = date_obj.strftime("%Y-%m-%d")
        else:
            publishing = "2024-01-01"

        is_ratingOk = browser.find_elements(By.CLASS_NAME, 'gd_rating')
        if is_ratingOk:
            rating = browser.find_element(By.CLASS_NAME, 'gd_rating').find_element(By.TAG_NAME, 'em').text
        else:
            rating = '0.0'

        is_reviewOk = browser.find_elements(By.CSS_SELECTOR, 'span.gd_reviewCount em.txC_blue')
        if is_reviewOk:
            review = browser.find_element(By.CLASS_NAME, 'gd_reviewCount').find_element(By.TAG_NAME, 'em').text
            review = int(review.replace(",", ""))
        else:
            review = 0
        sales = browser.find_element(By.CLASS_NAME, 'gd_sellNum').text.split(" ")[2]
        sales = int(sales.replace(",", ""))
        price = browser.find_element(By.CLASS_NAME, 'yes_m').text[:-1]
        price = int(price.replace(",", ""))
        
        is_full_textOk = browser.find_elements(By.CSS_SELECTOR, 'span.gd_best dd')
        if is_full_textOk:
            full_text = browser.find_element(By.CLASS_NAME, 'gd_best').find_element(By.TAG_NAME, 'dd').text
            parts = full_text.split(" | ") 
            ranking_part = parts[0]
            ranking = ''.join(filter(str.isdigit, ranking_part)) # 숫자만 추출
            if len(parts) > 1:
                ranking_weeks_part = parts[1]
                ranking_weeks = ''.join(filter(str.isdigit, ranking_weeks_part.split()[-1]))
            else:
                ranking_weeks = 0
        else:
            ranking = 0
            ranking_weeks = 0

        sql = """
                INSERT INTO Books(
                    title, author, publisher, publishing, rating, 
                    review, sales, price, ranking, ranking_weeks
                )
                VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                )
                """
        
        cursor.execute(sql, (title, author, publisher, publishing, rating, review, sales, price, ranking, ranking_weeks))
        conn.commit()

        time.sleep(2)