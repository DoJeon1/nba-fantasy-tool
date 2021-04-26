import requests
from bs4 import BeautifulSoup

URL = 'https://ca.indeed.com/jobs?q=software+developer&l=canada'
page = requests.get(URL)

html = BeautifulSoup(page.content, 'html.parser')
results = html.find(id='resultsCol')
jobPostings = results.find_all(class_='jobsearch-SerpJobCard')

#jobFile = open('job-data.txt', 'w')
import csv 
with open('job-data.csv', 'w', newline='') as file:
    jobFile = csv.writer(file)

    for posting in jobPostings:
        title = posting.find('a', class_='jobtitle')
        company = posting.find('span', class_='company')
        location = posting.find(class_='location')
        
        jobFile.writerow(title.text.strip())
        jobFile.writerow(company.text.strip())
        jobFile.writerow(location.text.strip())
        jobFile.writerow('\n')

        """
        Writing to a text file
        jobFile.write(title.text.strip() + "\n")
        jobFile.write(company.text.strip() + "\n")
        jobFile.write(location.text.strip() + "\n")
        jobFile.write("\n")
        """
