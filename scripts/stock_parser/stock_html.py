import config
from bs4.element import Comment
from bs4 import BeautifulSoup

import requests
import urllib.request
import export

def stock_access(login_info):
  with requests.Session() as session:
    session.post(config.login_url, data=login_info)
    hex_rpg_response = session.get(config.stock_url)
    text = hex_rpg_response.text
    return text

def parse_data(stock):
  soup = BeautifulSoup(stock, 'html.parser')
  texts = soup.findAll(text=True)
  visible_texts = filter(tag_visible, texts)
  data = u"\n".join(t.strip() for t in visible_texts)
  export.export(config.parsed_name)
  print(data)

def tag_visible(element):
  if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
      return False
  if isinstance(element, Comment):
      return False
  return True

