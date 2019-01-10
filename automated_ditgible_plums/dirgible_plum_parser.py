from bs4 import BeautifulSoup
from datetime import date

import calendar
import config
import requests
import re

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
            print("While you are here, I'll see if we need to purchase supplies for future plum farming.\n")
            #print("Alright, let me pull up a list of supplies you have right now and what can be purchased in the store.\n")
            plumSupplyPurchase(session, plumSupplyCheck(session))
            plumResupply(session)
            #print("Awesome! I finished purchasing everything and have moved the new supplies into your farm!\n")
            #print("I think I'm going to look into taking care of the plums we have now!\n")
            #print("Alright, let me see if we have any plums on the tree.\n")
            plumTreeCheck(session)

def plumTreeCheck(session):
    pass

def plumSupplyCheck(session):
    supply_array = []
    plumHTML = session.get(config.plum_url)
    # print(plumHTML.text)

    plumSoup = BeautifulSoup(plumHTML.text, 'html.parser')
    
    # this is an array 
    search_phrase = plumSoup.find_all("div", {"class": "meter"})
    
    # print(search_phrase)
    
    for supply in search_phrase:
        seperate_supply = supply.find_all("span")
        # print(seperate_supply)
        
        valueCheck = re.compile('\d+')
        #print(str(seperate_supply))

        supply_total = valueCheck.search(str(seperate_supply))
        
        current_supply = supply_total.group()
        supply_array.append(current_supply)

    return supply_array

def plumSupplyPurchase(session, supply_array):
    supply_index = 0
    for supply in supply_array:
        converted_supply = int(supply, 10)
        total_cost = 0
        if(converted_supply < 50):
            # print(supply_index)
            # print(converted_supply)

            if(supply_index == 0):
                print("It looks like you are in need of some water, I'll go ahead and purchase some and move it into your inventory.")
                session.post(config.water_url, config.water_info)
                total_cost = total_cost + 1200

                # this is the object that needs to be resupplied
                purchase = "water"

                plumResupply(session, purchase)


            if(supply_index == 1):
                print("It looks like you are in need of some plant food, I'll go ahead and purchase some and move it into your inventory.")
                session.post(config.food_url, config.food_info) 
                total_cost = total_cost + 600
                
                #this is the object that needs to be resupplied
                purchase = "food"

                plumResupply(session, purchase)

            if(supply_index == 2):
                print("It looks like you are in need of some plant fertilizer, I'll go ahead and purchase some and move it into your inventory.")
                session.post(config.fertilizer_url, config.fertilizer_info)
                total_cost = total_cost + 2000

                #this is the object that needs to be resupplied
                purchase = "fertilizer"

                plumResupply(session, purchase)

            if(supply_index == 3):
                print("It looks like you are in need of some plant soil, I'll go ahead and purchase some and move it into your inventory.")
                session.post(config.soil_url, config.soil_info)
                total_cost = total_cost + 500
                
                # this is the object that needs to be resupplied
                purchase = "soil"

                plumResupply(session, purchase)
            
        supply_index += 1
        print("I've finished purchasing your plum supplies where necessary. Feel free to verifiy my work. The total cost for this is " + str(total_cost) + " which has been deducted from you in hand money!")

def plumResupply(session, resupply):
    print("Hello! I assume that you have plum supplies in your inventory, so I will not work correctly if you do not.\n")
    print("Don't worry, I will let you know if something has a problem in the resupply process.")

    if(resupply == "water"):
        print("I see that you are in need of water! Never fear, I can refill it easily.")
        session.post(config.resupply_water_url, config.resupply_water_info)



plumPurchase(dateCheck())