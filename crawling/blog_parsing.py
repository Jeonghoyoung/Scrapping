from selenium import webdriver
from bs4 import BeautifulSoup
from tqdm import tqdm


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
keyword = '세종 카페'
url = f'https://search.naver.com/search.naver?query={keyword}&nso=&where=blog&sm=tab_opt'
driver.get(f'{url}')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
print(soup)