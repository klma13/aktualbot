# Import libraries


import requests
import time
from bs4 import BeautifulSoup
import re
import yagmail


from emails import emails
from emails import auth

# Set the URL you want to webscrape from
url = 'https://www.novinky.cz/zahranicni/svet'

print("Making a request to",url)

# Connect to the URL
response = requests.get(url)
print("Got index")

emailIndex = 0

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

for cell in soup.select('div.g_f1 > ul > li > div > div > div > a:nth-child(1)'):
  articleText = ""
  print(cell['href'])
  print("\n")

  responseAr = requests.get(cell['href'])
  soupAr = BeautifulSoup(responseAr.text, "html.parser")

  for textDiv in soupAr.select('h1.d_w'):
    articleText += "<h1>"+str(textDiv.getText()) + "</h1>"
    heading = str(textDiv)
  for textDiv in soupAr.select('.g_fY > p:nth-child(1)'):
    articleText += str(textDiv)

  for textDiv in soupAr.select('div.f_cH > p:nth-child(1)'):
    articleText += str(textDiv)

  #print(articleText)
  print("\n ====================================== \n")

  data = {
    "email": emails[emailIndex],
    "msg" : articleText
  }
  heading = heading.replace('<h1 class="d_w d_x">', '')
  heading = heading.replace('</h1>', '')

  print("Sending", heading,"to",data['email'])

  try:
      yag = yagmail.SMTP(auth[0],auth[1])
      yag.send('mackczgames@gmail.com', 'Aktualbot', data['msg'])
  except:
      print("Bruh")
  emailIndex += 1

  if len(emails) == emailIndex:
    break

if len(emails) > emailIndex:
  print("Bruh need moar")
