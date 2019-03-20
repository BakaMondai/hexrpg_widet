import config

import plum_supply_check as sup_check

def plum_supply_bool(session):
    supply_verification = sup_check.plum_supply_check(session)
    
    for supply in supply_verification:
        converted_supply = int(supply, 10)
        if(converted_supply > 50):
            # we do not need to resupply
            supply_bool = True
        else:
            # we do need to resupply
            supply_bool = False

    return supply_bool