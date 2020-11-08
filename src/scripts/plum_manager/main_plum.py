from bs4 import BeautifulSoup

import scripts.config as config
import scripts.login as login
import requests
import re

import day_of_week as day
import plum_purchase as purchase

import plum_resupply as resupply
import plum_supply_check as sup_check
import plum_supply_purchase as sup_purchase
import plum_tree_check as tree_check

# Right now, main is not going to do anything but cost me galleons, so don't run it if you don't have to. 
import plum_supply_bool as sup_bool

def plumStartUp():
    with requests.Session() as session:
    #login to the website
        session.post(config.login_url, data=config.login_info)

        print("You've logged into HexRPG. My name is PlumGuide. I handle everything plum related\n")
        print("Let me see if plums are available today...\n\n\n")

        day_check = day.dateCheck()

        if(sup_bool.plum_supply_bool(session) == True):
            #purchase.plum_purchase(session, day_check)
            print("This is bleep")
        else:
            #purchase_items = sup_check.plum_supply_check(session)
            #sup_purchase.plum_supply_purchase(session, purchase_items)
            pass



plumStartUp()