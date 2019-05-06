from bs4 import BeautifulSoup

import scripts.config as config
import re

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
