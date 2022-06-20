import re
from selenium import webdriver
from bs4 import BeautifulSoup
from tqdm import tqdm
import time


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
keyword = '세종 카페'
url = f'https://search.naver.com/search.naver?query={keyword}&nso=&where=blog&sm=tab_opt'
driver.get(f'{url}')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
title_info = soup.find_all('a', {'class':'api_txt_lines'})

blog_dict = {}
links, ttl = [], []
for title in title_info:
    link = title['href']
    post = title.get_text()
    links.append(link)
    ttl.append(post)

user_id = [l.split('/')[3] for l in links]
print(user_id)
print(ttl[:4])

for i in range(len(links)):
    driver.get(links[i])
    soc = driver.page_source
    soup = BeautifulSoup(soc, 'html.parser')
    real_url = f"https://blog.naver.com/{soup.iframe['src']}"
    print(real_url)

    driver.get(real_url)
    real_html = driver.page_source
    r_soup = BeautifulSoup(real_html, 'html.parser')
    text_in = r_soup.find_all(class_='se-module se-module-text')
    txt_list = [txt.get_text().strip().replace('\u200b', '') for txt in text_in]
    print(len(txt_list))

    with open(f'{user_id[i]}_{keyword}_text.txt', 'w') as f:

        f.write('\n'.join(txt_list))
    time.sleep(5)