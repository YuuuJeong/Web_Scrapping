import requests
from bs4 import BeautifulSoup


indeed = "https://indeed.com/jobs?q=python&limit=50&start=9999"

indeed_result = requests.get(indeed)

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")



pagination = indeed_soup.find("div", {"class" : "pagination"})

links = pagination.find_all('a')
pages = []

for link in links[1:]:
    pages.append(int(link.string))

max_page = pages[-1] + 1
print(max_page)
# commit
