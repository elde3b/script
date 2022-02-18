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
access_token = "EAADMxZAMrZCMYBAHARd62TgDQ0CVmgaVlnrZCapZBxWltB13ZADfGTzAsBH8Pd0duzPFqTxusm3YCNyyYZBS0r4ZB1by7k19jPsjog4HEWZABAJg3pu0fZApUkUWnBNSapbSVVg6urGZAXuESG6Vd9fZAKDDCQMMK4laKL03TNTULUUmgZDZD
"
############################################

asafb = fb.GraphAPI(access_token)

asafb.put_object("me", "feed", message = myTW)



