import requests
from bs4 import BeautifulSoup

URL = "https://www.linkedin.com/jobs/search/?geoId=101174742&keywords=software%20intern&location=Canada"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)