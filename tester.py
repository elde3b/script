import facebook as fb
from bs4 import BeautifulSoup as bs
import requests

try:
    myUrl = requests.get('https://nitter.net/AlMosahf')
    source = myUrl.content
    
    soup = bs(source, 'html.parser')
    twi = soup.find_all('div', {'class':'tweet-content'})
    
    myTW = twi[1].text
    if('pic.twitter.com' in myTW):
        myTW = twi[2].text
    else:
        myTW = twi[1].text


except:

    myUrl = requests.get('https://t.qbool.fr/AlMosahf')
    source = myUrl.content

    soup = bs(source, 'html.parser')

    twi = soup.find_all('div', {'class':'tweet-content'})
    myTW = twi[1].text
    if('pic.twitter.com' in myTW):
        myTW = twi[2].text
    else:
        myTW = twi[1].text


############################################
access_token = "EAADMxZAMrZCMYBACob61xjUse1LO8H5IyilocDM0m091pW0q0YJ3eic81W1c7qjFDiiZCBVUepdrtIBBCcVYH8EeSdmRoIiuBPMr4IihGzUELfzbss7UwaMLd8ZBGCBNZBtWHZA5r4Y66GrBmnEy3R7iC93l7Ez6sdkx8sGAV0iQZDZD
"
############################################

asafb = fb.GraphAPI(access_token)

asafb.put_object("me", "feed", message = myTW)



