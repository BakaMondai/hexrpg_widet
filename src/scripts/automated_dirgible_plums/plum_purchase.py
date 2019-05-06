from bs4 import BeautifulSoup

import config

import plum_purchase as purchase
import day_of_week as day

dayOfWeek = day.dateCheck()

def plum_purchase(session, dayOfWeek):
    if dayOfweek == "Sunday":
        for i in range(0,1):
            session.post(config.cart_url, config.plum_info)
            print("Purchased plum number " + str(i + 1))

            plum_page = session.get(config.plum_purchase_url)
            new_plum = BeautifulSoup(plum_page.text, 'html.parser')

            search_phrase = new_plum.find("div", {"id": "mainContent"})
            # print(search_phrase)

            plum = search_phrase.find_all("table")
            # print(plum)


            re.compile('\d+')

    else:
        print("Today is " + dayOfweek + ". I can't purchase plums until Sunday. Sorry!\n")
        print("While you are here, I'll see if we need to purchase supplies for future plum farming.\n")
        #print("Alright, let me pull up a list of supplies you have right now and what can be purchased in the store.\n")
        plumSupplyPurchase(session, plumSupplyCheck(session))
        #print("Awesome! I finished purchasing everything and have moved the new supplies into your farm!\n")
        #print("I think I'm going to look into taking care of the plums we have now!\n")
        #print("Alright, let me see if we have any plums on the tree.\n")
        plumTreeCheck(session)
