from src.db import DB
import requests
from bs4 import BeautifulSoup

def scrape(id):
  DB.pages().update('True', id)
  url = DB().pages().fetch(id)
  page = requests.get(url[0])
  soup = BeautifulSoup(page.text, features='html.parser')
  a_soup = soup.find_all('a', href=True)
  ext_links = [link.get("href") for link in a_soup if "http" in link.get("href")]
  new_links = ext_links[:10]
  DB.links().delete(id)
  for i in new_links:
    DB.links().insert(i, id)




