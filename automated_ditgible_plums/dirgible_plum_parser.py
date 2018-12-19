from bs4 import BeautifulSoup
from datetime import date

import calendar
import config
import requests

def dateCheck():
    # what is today?
    my_date = date.today()
    today = calendar.day_name[my_date.weekday()]

    return today

def plumPurchase(dayOfweek):
    with requests.Session() as session:
    #login to the website
        session.post(config.login_url, data=config.payload)

        print("You've logged into HexRPG. My name is PlumGuide. I handle everything plum related\n")
        print("Let me see if plums are available today...\n\n\n")

        if dayOfweek == "Sunday":
            for i in range(0,5):
                session.post(config.cart_url, config.plum_info)
                print("Purchased plum number " + i)
        else:
            print("Today is " + dayOfweek + ". I can't purchase plums until Sunday. Sorry!\n")
            print("While you are here, I'll purchase the required supplies for future plum farming.\n")
        
            print("Alright, let me pull up a list of supplies you have right now and what can be purchased in the store.\n")
            plumSupplyPurchase(session)
            plumResupply(session)
            print("Awesome! I finished purchasing everything and have moved the new supplies into your farm!\n")
            print("I think I'm going to look into taking care of the plums we have now!\n")
            print("Alright, let me see if we have any plums on the tree\n")
            plumTreeCheck(session)

def plumTreeCheck(session):
    pass

def plumSupplyPurchase(session):
    pass

def plumResupply(session):






plumPurchase(dateCheck())