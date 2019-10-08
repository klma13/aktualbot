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
print("Finished")
# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
for i in range(36,len(soup.findAll('a', {"class": "d_aq"}))): #'a' tags are for links
    one_a_tag = soup.findAll('a', {'class': "d_aq"})[i]
    link = one_a_tag['href']
    print(link)
   	#download_url = 'http://web.mta.info/developers/'+ link
  	#urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 
    time.sleep(0.01) #pause the code for a sec