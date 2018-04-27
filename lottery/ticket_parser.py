import requests
import urllib.request
import export
import config
from bs4.element import Comment
from bs4 import BeautifulSoup

def lottery_access(login_info, posting_info):
  for i in range(0, config.counter, 1):
    with requests.Session() as session:
      #login to the website
      session.post(config.login_url, data=login_info)

      #request the information from the url
      hex_rpg_response = session.get(config.lottery_url)
    
      #post our  information to the lottery ticket page
      hex_rpg_lottery_post = session.post(config.lottery_url, data=posting_info)
      print(f"Purchased ticket: {i + 1}")

lottery_access(config.login_info, config.purchase_post)