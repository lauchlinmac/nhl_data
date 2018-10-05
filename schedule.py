import json, urllib.request,requests, datetime
# This gives the schedule for the date listed
#input should be team selection, submitted by id

#set the base URL
base_url = 'https://statsapi.web.nhl.com/api/v1/'

current_day = datetime.date.today()
test_day = datetime.date(2018, 10, 11)
print(test_day)
threeDays = current_day+datetime.timedelta(days = 10)
#print(current_day)
#print(threeDays)


fav_team = 1

nhl_data = base_url+'schedule?teamId='+str(fav_team)+'&startDate='+str(current_day)+'&endDate='+str(threeDays)
test_nhl_data = base_url+'schedule?&date='+str(test_day)+'&teamId='+str(fav_team)
json_data = requests.get(nhl_data).json()
print(test_nhl_data)
print(nhl_data)
test_json_data = requests.get(test_nhl_data).json()
isGame = test_json_data['totalGames']

print(isGame)


number = len(json_data['dates'])

i=0 
while i < number:
    away_team = json_data['dates'][i]['games'][0]['teams']['away']['team']['name']
    home_team = json_data['dates'][i]['games'][0]['teams']['home']['team']['name']
    game_date = json_data['dates'][i]['games'][0]['gameDate']
    print('Game Date:',game_date)
    print('Home Team:',home_team)
    print('Away Team:',away_team)
    i=i+1

print('There are',number,'games in the period searched.')