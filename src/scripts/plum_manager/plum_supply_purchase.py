import config as config

import plum_resupply as resupply

# this file will only be called if the original main_plum check fails

def plum_supply_purchase(session, supply_array):
    supply_index = 0
    for supply in supply_array:
        converted_supply = int(supply, 10)
        total_cost = 0
        if(converted_supply <= 50):
            # print(supply_index)
            # print(converted_supply)

            if(supply_index == 0):
                print("It looks like you are in need of some water, I'll go ahead and purchase some and move it into your inventory.")
                #session.post(config.water_url, config.water_info)
                total_cost = total_cost + 1200

                # this is the object that needs to be resupplied
                purchase = "water"

                resupply.plum_resupply(session, purchase)


            if(supply_index == 1):
                print("It looks like you are in need of some plant food, I'll go ahead and purchase some and move it into your inventory.")
                #session.post(config.food_url, config.food_info) 
                total_cost = total_cost + 600
                
                #this is the object that needs to be resupplied
                purchase = "food"

                resupply.plum_resupply(session, purchase)

            if(supply_index == 2):
                print("It looks like you are in need of some plant fertilizer, I'll go ahead and purchase some and move it into your inventory.")
                #session.post(config.fertilizer_url, config.fertilizer_info)
                total_cost = total_cost + 2000

                #this is the object that needs to be resupplied
                purchase = "fertilizer"

                resupply.plum_resupply(session, purchase)

            if(supply_index == 3):
                print("It looks like you are in need of some plant soil, I'll go ahead and purchase some and move it into your inventory.")
                #session.post(config.soil_url, config.soil_info)
                total_cost = total_cost + 500
                
                # this is the object that needs to be resupplied
                purchase = "soil"

                resupply.plum_resupply(session, purchase)

        supply_index += 1
        
        print("I've finished purchasing your plum supplies where necessary. Feel free to verifiy my work. The total cost for this is " + str(total_cost) + " which has been deducted from you in hand money!")
