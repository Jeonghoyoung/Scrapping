import requests
from bs4 import BeautifulSoup

limit = 5
keyword = 'python'
url = f'https://www.indeed.com/jobs?q={keyword}&limit={limit}'


def extract_indeed_pages(url):
    indeed_result = requests.get(url)
    soup = BeautifulSoup(indeed_result.text, 'html.parser')
    pagination = soup.find('div', {'class': 'pagination'})
    pages = pagination.find_all('a')
    print(pages)

    spans = [int(p.string) for p in pages[:-1]]
    max_page = spans[-1]
    return max_page


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{url}&start={0 * limit}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "heading4"})
        for result in results:
            title = result.find("h2", {"class": "jobTitle"}).find("span", title=True).string
            jobs.append(title)
    return jobs


print(extract_indeed_jobs(1))
