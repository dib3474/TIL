import os
import requests


def URL(url):
    url = url.lower().strip()
    if 'http' not in url:
      url = "http://" + url    
    return url

def main():
  while True:
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
    while True:
      exit_check = input("Do you want to start over? y/n ")
      if exit_check == 'y' or exit_check == 'n':
        break
      else:
        print("That's not a valid answer")
    if exit_check == 'y':
      continue
    else:
      print("k. bye!")
      break

if __name__ == '__main__':
  main()