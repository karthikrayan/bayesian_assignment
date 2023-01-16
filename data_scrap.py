import requests
import time 
import json

global datalist
global count
count = 0
datalist = list()

def print_data():
  url = "https://api.coindesk.com/v1/bpi/currentprice.json"
  response = requests.get(url)
  data = response.json()
  datalist.append(data)
  global count
  count = count + 1
  print(data)

import schedule
schedule.every(5).minutes.do(print_data)
print(schedule.get_jobs())

while count<290:
    schedule.run_pending()
    jsonString = json.dumps(datalist)
    jsonFile = open("data.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
    if len(datalist)==290:
      break

print(datalist)
  
# jsonString = json.dumps(datalist)
# jsonFile = open("data.json", "w")
# jsonFile.write(jsonString)
# jsonFile.close()