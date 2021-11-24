import requests
import json


lboards = ['barbarian', 'monk','dh', 'wd', 'wizard','crusader', 'team-2', 'team-3', 'team-4']

def main():
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
        for run in data:
            if "team" in lb:
                if run['rift_data']['api_rank'] == 1:
                        format_team_best(run)
                        print("\n\nTop BriTs :")
                for player in run['player_data']:
                    if player.get('ctag') == "BriT" and \
                        player.get('cname') == "BriTon" and \
                        clan_rank < 5:
                        clan_rank += 1
                        if clan_rank > 1 : print("\n")
                        format_team_rank(clan_rank, run)
                        break
            else:
                if run['rift_data']['api_rank'] == 1:
                    format_solo_best(run)
                    print("\n\nTop BriTs :")
                elif 'ctag' in run['player_data'][0]:
                    if run['player_data'][0]['ctag'] == "BriT" and \
                        run['player_data'][0]['cname'] == "BriTon" and \
                        clan_rank < 5:
                        clan_rank += 1
                        format_solo_rank(clan_rank, run)

def format_solo_best(run):
    print(f">> 1er: {run['player_data'][0]['btag']}\
({run['player_data'][0].get('ctag','<Pas de clan>')}) \
p{run['player_data'][0]['plvl']} \
-> GR{run['rift_data']['grlvl']} \
en {run['rift_data']['time']}")

def format_solo_rank(cr, run):
    print(f"#{cr} : {run['player_data'][0]['btag']} \
p{run['player_data'][0]['plvl']} \
-> GR{run['rift_data']['grlvl']} \
en {run['rift_data']['time']}")

def format_team_best(run):
    print(f">> 1er: GR{run['rift_data']['grlvl']} en {run['rift_data']['time']}")
    for p in run['player_data']:
        print(f"-> [{p['class']}] {p['btag']}({p.get('ctag','<Pas de clan>')}) - p{p['plvl']}")

def format_team_rank(cr, run):
    print(f"#{cr} : GR{run['rift_data']['grlvl']} en {run['rift_data']['time']}")
    for p in run['player_data']:
        print(f"-> [{p['class']}] {p['btag']}({p.get('ctag','<Pas de clan>')}) - p{p['plvl']}")

if __name__ == "__main__":
    main()