import requests
import urllib.request
import config
import random
import time

def ticket(login_info, posting_info):
  while True:
    try:
      index = int(input("Enter an integer: "))
    except ValueError:
      print("Not an integer!")
      continue
    else:
      print("Yes an integer!")
      break 

  with requests.Session() as session:
    #login to the website
    session.post(config.login_url, data=config.login_info)
    
    try:
      for i in range(0, index, 1):
        randNum = random.randint(0, 2)
        if (randNum >= 1):
          #post our information to the lottery ticket page
          session.post(config.lottery_url, data=posting_info)
          print(f"Purchased ticket: {i + 1}")
          print(f"Total Galleons used in this session: {(i + 1) * 500 }")
          time.sleep(randNum)
          print(f"Waiting for {randNum} second")
        else:
          #post our information to the lottery ticket page
          session.post(config.lottery_url, data=posting_info)
          print(f"Purchased ticket: {i + 1}")
          print(f"Total Galleons used in this session: {(i + 1) * 500 }")

    except:
      print(f"Ticket purchase failed last ticket successfully puchased {i + 1}")  

ticket(config.login_info, config.purchase_post)
