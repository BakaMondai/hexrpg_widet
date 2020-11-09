from bs4 import BeautifulSoup

import config as config
import requests
import re

import day_of_week as day
import plum_purchase as purchase
import plum_resupply as resupply
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

        #  Can only purchase plums on Sunday's 
        if(day_check == "Sunday"):
            
            # Determine if plums have been purchased before hand
            # true means the tree is full
            if(sup_bool.plum_purchase_bool(session) == True):

                sup_bool.plum_purchase_check(session)

                #purchase.plum_purchase(session, day_check)
                print("This is bleep")
            else:
                #purchase_items = sup_check.plum_supply_check(session)
                #sup_purchase.plum_supply_purchase(session, purchase_items)
                pass
        else:
            pass
# Determine if the supplies are full 
# if(sup_bool.plum_supply_bool(session) == True):

plumStartUp()