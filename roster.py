import json, urllib.request,requests
# This app pulls the roster to the team ID in ti

#set the base URL
base_url = 'https://statsapi.web.nhl.com/api/v1/'

ti = 22

nhl_data = base_url+'teams/'+str(ti)+'/roster'
team_name = base_url+'teams/'+str(ti)
# This is a good version of getting the roster - need to sort*/
json_data = requests.get(nhl_data).json()
team_data = requests.get(team_name).json()

number = len(json_data['roster'])
i=0
players = []

while i < number:
    players.append(json_data['roster'][i]['person']['fullName'])
    i=i+1
    players.sort()
t_name = team_data['teams'][0]['name']
print('There are',number,'players on the',t_name)
print('---------------------------------------')
i=0
while i < number:
    print(players[i]) 
    i=i+1

