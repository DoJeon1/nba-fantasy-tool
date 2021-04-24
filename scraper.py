import requests
from bs4 import BeautifulSoup

URL = 'https://ca.indeed.com/jobs?q=software+developer&l=canada'
page = requests.get(URL)

html = BeautifulSoup(page.content, 'html.parser')
results = html.find(id='resultsCol')
jobPostings = results.find_all(class_='jobsearch-SerpJobCard')

for posting in jobPostings:
    title = posting.find('a', class_='jobtitle')
    company = posting.find('span', class_='company')
    #location = posting.find('div', class_='location accessible-contrast-color-location')
    location = posting.find(class_='location')
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print()
