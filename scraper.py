import requests
from bs4 import BeautifulSoup

URL = 'https://ca.indeed.com/jobs?q=software+developer&l=canada'
page = requests.get(URL)

html = BeautifulSoup(page.content, 'html.parser')
results = html.find(id='resultsCol')
jobPostings = results.find_all(class_='jobsearch-SerpJobCard')

for posting in jobPostings:
    title = posting.find('h2', class_='title')
    company = posting.find('span', class_='company')
    #location = posting.find('div', class_='recJobLoc')
    print(title.text)
    print(company.text)
    #print(location.text)
    print()
