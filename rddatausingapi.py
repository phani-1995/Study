import requests
import json
import csv
try:
    api = "https://api.covid19india.org/data.json"
    response = requests.get(api)
    print(response.status_code)
    data = response.json()
    print(data)
    print("data read sucessfully")
except:
    print("Data not read sucessfully")


data1 = data['statewise']
for msg in data1:
    res = json.loads(msg.value.decode('utf-8'))
    dlist = list(res.values())
    print(dlist)
 