from selenium import webdriver
from bs4 import BeautifulSoup
from tqdm import tqdm


def main():
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.implicitly_wait(3)
    keyword = '세종 카페'
    url = f'https://search.naver.com/search.naver?query={keyword}&nso=&where=blog&sm=tab_opt'
    driver.get(f'{url}')
    # req = driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    src = soup.find_all('iframe')[0]['src']
    htmls = f'http://blog.naver.com/{src}'
    driver.get(htmls)

    soc = driver.page_source
    soup = BeautifulSoup(soc, 'html.parser')
    a = soup.find_all(class_='se-module se-module-text')

    txt_list = []
    for i in tqdm(a):
        #         print(i.get_text())
        txt = i.get_text().strip().replace('\u200b', '')
        txt_list.append(txt)

    driver.close()
    # 텍스트 파일로 다운로드.
    with open('crawling_data.txt', 'w') as f:

        f.write('\n'.join(txt_list))

if __name__ == '__main__':
    main()