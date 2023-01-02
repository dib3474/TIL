import csv

def save_to_file(jobs, word):
  file = open(f"{word}.csv", mode="w")
  print(file)
  w = csv.writer(file)
  w.writerow(["title", "company", "location", "link"])
  for job in jobs:
    w.writerow(list(job.values()))
  return