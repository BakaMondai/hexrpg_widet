from bs4 import BeautifulSoup

import config as config

import plum_purchase as purchase
import day_of_week as day

dayOfWeek = day.dateCheck()

def plum_purchase(session, dayOfWeek):
    if dayOfweek == "Sunday":
        for i in range(0,1):
            session.post(config.cart_url, config.plum_info)


            plum_page = session.get(config.plum_purchase_url)
            new_plum = BeautifulSoup(plum_page.text, 'html.parser')

            search_phrase = new_plum.find("div", {"id": "mainContent"})
            plum = search_phrase.find_all("table")



            re.compile('\d+')

    else:
        plumSupplyPurchase(session, plumSupplyCheck(session))
        plumTreeCheck(session)
