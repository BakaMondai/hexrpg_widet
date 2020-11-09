from bs4 import BeautifulSoup

import re
import config as config

# Check the current supply level of the plum supplies
def plum_supply_bool(session):
    supply_verification = plum_supply_check(session)
    
    for supply in supply_verification:
        converted_supply = int(supply, 10)
        if(converted_supply > 50):
            # we do not need to resupply
            supply_bool = True
        else:
            # we do need to resupply
            supply_bool = False

    return supply_bool

# Check to see if plums are already in the tree
# return true if the plums have been previously purchased
def plum_purchase_bool(session):
    return True

    

# look at the content of the page to determine the number of plums
def plum_purchase_check(session):

    supply_array = []

    plumHTML = session.get(config.plum_url)

    plumSoup = BeautifulSoup(plumHTML.text, 'html.parser')

    search_phrase = plumSoup.find_all("div", {"class": "plum5"})

    if(search_phrase):
        print("There are five plums in the plum tree.")
    else: 
        print("More plums must be purchased!")
        

# look at the content of the page and determine the amount of plum supplies
def plum_supply_check(session):
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

