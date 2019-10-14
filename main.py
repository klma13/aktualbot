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
   	#download_url = 'http://web.mta.info/developers/'+ link
  	#urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 
