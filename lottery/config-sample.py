counter = 5

login_url = "" # use if the webpage you want is behind a login url
lottery_url = "" 

# this will vary by site, use the inspector tool to fill them in if need be (search for hidden input tags)
login_info = {
  "username":"",
  "password":"",
  "action":"",
  "sid":""
}

purchase_post = {
  "buy":"1",
  "g":"100",
  "s":"0",
  "k":"0",
  "submit":"   Pay   "
}
start_condition = 0
end_condition = 1000