import json, urllib.request,requests
# This gives the schedule for the date listed

#set the base URL
base_url = 'https://statsapi.web.nhl.com/api/v1/'

fav_team = 30
nhl_data = base_url+'schedule?teamId='+str(fav_team)+'&startDate=2018-12-01&endDate=2018-12-31'

json_data = requests.get(nhl_data).json()


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