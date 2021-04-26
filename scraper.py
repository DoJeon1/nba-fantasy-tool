import requests
from bs4 import BeautifulSoup

URL = 'https://ca.indeed.com/jobs?q=software+developer&l=canada'
page = requests.get(URL)

html = BeautifulSoup(page.content, 'html.parser')
results = html.find(id='resultsCol')
jobPostings = results.find_all(class_='jobsearch-SerpJobCard')

jobFile = open('job-data.txt', 'w')

for posting in jobPostings:
    title = posting.find('a', class_='jobtitle')
    company = posting.find('span', class_='company')
    location = posting.find(class_='location')
    
    jobFile.write(title.text.strip() + "\n")
    jobFile.write(company.text.strip() + "\n")
    jobFile.write(location.text.strip() + "\n")
    jobFile.write("\n")
    """
    Printing to the command line ...
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print()
    """

jobFile.close()