import requests
import json

lboards = ['barbarian', 'monk','dh', 'wd', 'wizard','crusader', 'team-2']

for lb in lboards:
    # Récupération de chaque flux classement sur maxroll.gg
    url =f'https://assets.maxroll.gg/leaderboards/s24-eu-rift-hardcore-{lb}.json'
    response = requests.get(url)
    # Instanciation du String JSON dans un Dict
    json_data = json.loads(response.content)
    data = json_data["data"]
    # Initialisation du compteur classement Top BriT
    clan_rank = 0
    # Print en-tête titre classement
    print(f"\n-------------------------\nClassement hardcore-{lb} :")
    if "team" in lb:
        # print à factoriser vers une méthode dédiée
        for i in data:
            for p in i['player_data']:
                print(p)
            break
    else:
        for i in data:
            # print à factoriser vers une méthode dédiée
            if i['rift_data']['api_rank'] == 1:
                print(f">> 1er: {i['player_data'][0]['btag']}\
({i['player_data'][0].get('ctag','<Pas de clan>')}) \
-> GR{i['rift_data']['grlvl']} \
en {i['rift_data']['time']}\
\n\nTop BriTs :")
            elif 'ctag' in i['player_data'][0]:
                if i['player_data'][0]['ctag'] == "BriT" and \
                    i['player_data'][0]['cname'] == "BriTon" and \
                    clan_rank < 5:
                    clan_rank += 1
                    print(f"#{clan_rank} : {i['player_data'][0]['btag']} \
-> GR{i['rift_data']['grlvl']} \
en {i['rift_data']['time']}")
