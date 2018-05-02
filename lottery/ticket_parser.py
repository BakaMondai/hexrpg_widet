import requests
import urllib.request
import export
import time
import config
from bs4.element import Comment
from bs4 import BeautifulSoup

def lottery_access(login_info, posting_info):
  while True:
    try:
      counter = int(input("Enter something: "))
    except ValueError:
      print("Not an integer!")
      continue
    else:
      print("Yes an integer!")
      break 


  with requests.Session() as session:
    #login to the website
    session.post(config.login_url, data=login_info)
    
    for i in range(0, counter, 1):
      #post our  information to the lottery ticket page
      session.post(config.lottery_url, data=posting_info)
      print(f"Purchased ticket: {i + 1}")    

lottery_access(config.login_info, config.purchase_post)