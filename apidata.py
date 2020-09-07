import requests
import json
import csv

api = "https://api.covid19india.org/data.json"
response = requests.get(api)
data = response.json()
print(data)

fname = "output.csv"

with open(fname, "w") as file:
    csv_file = csv.writer(file)
    csv_file.writerow(['active', 'confirmed', 'deaths', 'recovered', 'state', 'statecode'])
    for item in data['statewise']:
        csv_file.writerow([item['active'], item['confirmed'], item['deaths'], item['recovered'], 
                           item['state'], item['statecode']])
        