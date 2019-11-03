import requests
import time
from bs4 import BeautifulSoup
import re
import yagmail


from emails2 import emails
from emails import auth

# Set the URL you want to webscrape from
url = 'https://www.novinky.cz/kultura'

print("Making a request to",url)

# Connect to the URL
response = requests.get(url)
print("Got index")

emailIndex = 0

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

for cell in soup.select('div.g_fW:nth-child(2) > ul > li > div > div > div > a:nth-child(1)'):
  print("article got")
  articleText = ""
  print(cell['href'])
  print("\n")

  responseAr = requests.get(cell['href'])
  soupAr = BeautifulSoup(responseAr.text, "html.parser")

  for textDiv in soupAr.select('h1.d_w'):
    articleText += "<h1>"+str(textDiv.getText()) + "</h1>"
    heading = str(textDiv)
  for textDiv in soupAr.select('.g_fS > p:nth-child(1)'):
    articleText += str(textDiv)

  for textDiv in soupAr.select('div.f_cP > p:nth-child(1)'):
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
      yag.send(data['email'], 'Aktualbot', data['msg'])
      #yag.send("mackczgames@gmail.com", 'Aktualbot', data['msg'])
      emailIndex += 1

  except:
      print("Bruh")

# if len(emails) == emailIndex:
#   break

if len(emails) > emailIndex:
  if (len(emails) - emailIndex)-1 > 0:
    print("Bruh need more articles for " +str(emails[emailIndex]) +" and "+ str((len(emails) - emailIndex)-1)+ " more")
  else:
    print("Bruh need one more article for " +str(emails[emailIndex]))
