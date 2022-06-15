import requests
from bs4 import BeautifulSoup

limit = 5
keyword = 'python'
url = f'https://www.indeed.com/jobs?q={keyword}&limit={limit}'
indeed_result = requests.get(url)
# print(indeed_result.text)
# .text : html의 모든 정보

soup = BeautifulSoup(indeed_result.text, 'html.parser')

pagination = soup.find('div', {'class': 'pagination'})
# print(pagination)
pages = pagination.find_all('a')
print(pages)

spans = [int(p.string) for p in pages[:-1]]
max_page = spans[-1]

jobs = []
for s in range(max_page):
    result = requests.get(f'{url}&start={s * limit}')
    print(result.status_code)