import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python"

def get_last_page():
  r = requests.get(URL)
  soup = BeautifulSoup(r.text, "html.parser")
  pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
  last_page = pages[-2].text.strip()
  return int(last_page)

def extarct_job(html):
  title = html.find("div", {"class": "flex--item fl1"}).find("h2").find("a")["title"]
  
  company, location = html.find("h3", {"class": "mb4"}).find_all("span", recursive=False)

  company = company.get_text(strip=1)
  location = location.get_text(strip=1)
  
  job_id = html["data-jobid"]

  return {
    'title': title,
    'company': company,
    'location': location,
    'link': f"https://stackoverflow.com/jobs/{job_id}"
  }


def extarct_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping SO: page: {page}")
    r = requests.get(f"{URL}&pg={page + 1}")
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find_all("div", {"class": "-job"})
    for result in results:
      job = extarct_job(result)
      jobs.append(job)
  return jobs

def get_jobs():
  last_page = get_last_page()
  jobs = extarct_jobs(last_page)
  
  return jobs