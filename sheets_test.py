import json, urllib.request,requests, datetime

#sheets ID for the Three Stars Sheet
sheet_ID = '1W8JClH8gQg9HlmZJzrI6UJc3K6HcSeafECtNf9r5_bE'

base_url = 'https://sheets.googleapis.com/v4/spreadsheets/'

sheet_json = requests.get(base_url+sheet_ID+'/values/Sheet1!A1:D5?APIkey=AIzaSyB1z0U4nGihiCfIkAvaxwKjv7eJUu30u_E').json()

print(sheet_json)