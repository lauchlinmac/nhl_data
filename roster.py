import json, urllib.request,requests
nhl_data = 'https://statsapi.web.nhl.com/api/v1/teams/1/roster'

# This is a good version of getting the roster - need to sort*/
json_data = requests.get(nhl_data).json()

number = len(json_data['roster'])
i=0
players = []

while i < number:
    players.append(json_data['roster'][i]['person']['fullName'])
    i=i+1
    players.sort()

print('There are',number,'players on the team.')
print('----------------------------------')
i=0
while i < number:
    print(players[i])
    i=i+1

