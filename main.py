# Import libraries


import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'https://www.novinky.cz/zahranicni/svet'
print("Making a request to",url)
# Connect to the URL
response = requests.get(url)
print("Got index")
# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

for cell in soup.select('div.g_f1 > ul > li > div > div > div > a:nth-child(1)'):
  print(cell['href'])
  responseAr = requests.get(cell['href'])
  soupAr = BeautifulSoup(responseAr.text, "html.parser")
  for textDiv in soupAr.select('div.f_cH > p:nth-child(1)'):
    articleText += str(textDiv)

  print(articleText)
  print("\n ====================================== \n")

  emailReUrl = "https://hook.integromat.com/9k5llgs07x7mzm4m89g7l6fdt40p8o3g"
  data = {
    "email": "filip.tronicek@seznam.cz",   
    "msg" : articleText
  }
  #requests.post(emailReUrl, data=data, allow_redirects=True)
