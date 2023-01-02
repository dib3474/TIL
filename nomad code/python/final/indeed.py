import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def get_last_pages():
  result = requests.get(URL)

  soup = BeautifulSoup(result.text, "html.parser")

  pagination = soup.find("div", {"class": "pagination"})

  links = pagination.find_all('a')

  pages = []
  for link in links[:-1]:
    pages.append(int(link.string))

  max_page = pages[-1]
  return max_page

def extract_job(html):
  job_title = html.find("h2",{"class": "jobTitle"}).find("span", title=True).string

  company = html.find("span", {"class": "companyName"}).string
  #if title == "new":
  #  job_tilte = title.find_all("span")[1].string
  location = html.select_one("pre > div").text
  #location = html.find("div", {"class": "companyLocation"}).string  - > 이름이 긴 경우 None이 됨.

  job_id = html.parent['data-jk']

  return {
    'title': job_title, 
    'company': company, 
    'location': location,
    'link': f"https://www.indeed.com/viewjob?jk={job_id} "
  }

def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping Indeed: page {page}")
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "slider_container"})
    for title in results:
      job = extract_job(title)
      jobs.append(job)
  return jobs

def get_jobs():

  last_page = get_last_pages()

  jobs = extract_indeed_jobs(last_page)
  return jobs