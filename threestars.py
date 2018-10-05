import json, urllib.request,requests, datetime


# add base url
base_url = 'https://statsapi.web.nhl.com/api/v1/'

# set URL for previous game and 3 stars info
prev_game = '?expand=team.schedule.previous'

#set team
team_ID = '5'

#get the last game's ID
last_game_url = base_url+'teams/'+team_ID+prev_game
last_game_json = requests.get(last_game_url).json()

last_game_link = last_game_json['teams'][0]['previousGameSchedule']['dates'][0]['games'][0]['link']
team_name = last_game_json['teams'][0]['name']

game_url = 'https://statsapi.web.nhl.com'+last_game_link

#print(game_url)
game_json = requests.get(game_url).json()

# If the previous game doesn't exist, this doesn't work.
firstStar = game_json['liveData']['decisions']['firstStar']['fullName']
secondStar = game_json['liveData']['decisions']['secondStar']['fullName']
thirdStar = game_json['liveData']['decisions']['thirdStar']['fullName']

print('Team Name: ',team_name)
print('Last Game')
print('First Star: ',firstStar)
print('Second Star: ',secondStar)
print('Third Star: ',thirdStar)