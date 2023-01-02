import os
import requests


def URL(url):
    url = url.lower().strip()
    if 'http' not in url:
      url = "http://" + url    
    return url

def exit_check():
  while True:
    exit = input("Do you want to start over? y/n ")
    if exit == "y":
      return 1
      break
    elif exit == "n":
      print("k. bye!")
      return 0
      break
    else:
      print("That's not a valid answer")

exit_flag = 1
while exit_flag:
  os.system('clear')
  print("Welcome to IsItDown.py!")
  input_url = input("Please write a URL or URLs you want to check. (separated by comma)\n")
  urls = input_url.split(',')
  for url in urls:
    try:
      r = requests.get(URL(url))
      if r.status_code == 200:
        print(f"{URL(url)} is up!")
      elif r.status_code == 404:
        print(f"{URL(url)} is down!")
    except:
      if "." in url:
        print(f"{URL(url)} is down!")
      else:
        print(f"{url} is not valid URL")
  exit_flag = exit_check()