uniqueCounter = 1
unique_id = str(uniqueCounter + 1) 

parsed_name = "parsed_data.txt"
doc_name = "export_" + unique_id + ".csv"

start_condition = 510
end_condition = 697

login_url = "https://www.hexrpg.com/login.php" # use if the webpage you want is behind a login url
betting_url = "https://www.hexrpg.com/ra/bet.php?color=V" 
lottery_url = "https://www.hexrpg.com/store/store.php?store_id=1&item_id=233" 
stock_url = "https://www.hexrpg.com/stock/" # actual page you are searching for

# this will vary by site, use the inspector tool to fill them in if need be (search for hidden input tags)
login_info = {
  "username":"BakaMondai",
  "password":"Tomis50diary",
  "action":"submit",
  "sid":"e698fecc0b8a4545952c25ec748cac35"
}

bet_post = {
    "action":"confirm",
    "symbol":"0",
    "type":"V",
    "cellTitle":"Color",
    "iDisplay":"bet/violet.png",
    "galleon":"1000",
    "submit":"  Next > >  "
}

purchase_post = {
  "buy":"1",
  "g":"500",
  "s":"0",
  "k":"0",
  "submit":"   Pay   "
}