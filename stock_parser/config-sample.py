import time
import datetime

unique_id = str(datetime.datetime.now())

parsedName = "parsed_data.txt"
docName = "formatted_data.txt"
exportedName = "export_" + unique_id + ".csv"

login_url = "" # use if the webpage you want is behind a login url
stock_url = "" # actual page you are searching for

# this will vary by site, use the inspector tool to fill them in if need be (search for hidden input tags)
payload = {
  "username":"",
  "password":"",
  "action":"",
  "checkbox":"",
  "sid":""
}
