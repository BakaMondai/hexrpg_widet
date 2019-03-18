from bs4 import BeautifulSoup
import requests

import config

import day_of_week as day
import plum_purchase as purchase

import plum_resupply as resupply
import plum_supply_check as sup_check
import plum_supply_purchase as sup_purchase
import plum_tree_check as tree_check

def plum_purchase(session, dayOfWeek):
    if dayOfWeek == "Sunday":
        for i in range(0,1):
            session.post(config.cart_url, config.plum_info)
            print("Purchased plum number " + str(i + 1))

            plum_page = session.get(config.plum_purchase_url)
            new_plum = BeautifulSoup(plum_page.text, 'html.parser')

    else:
        print("Today is " + dayOfWeek + ". I can't purchase plums until Sunday. Sorry!\n")
        print("While you are here, I'll see if we need to purchase supplies for future plum farming.\n")
        # print("Alright, let me pull up a list of supplies you have right now and what can be purchased in the store.\n")
        
        #sup_purchase.plum_supply_purchase(session, sup_check.plum_supply_check(session))
        # print("Awesome! I finished purchasing everything and have moved the new supplies into your farm!\n")
        # print("I think I'm going to look into taking care of the plums we have now!\n")
        # print("Alright, let me see if we have any plums on the tree.\n")
        # tree_check.plum_tree_check(session)
