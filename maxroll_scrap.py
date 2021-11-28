import requests
import json


def get_current_season():
    url = 'https://assets.maxroll.gg/leaderboards/leaderboard_index.json'
    response = requests.get(url)
    data = json.loads(response.content)
    return data['season']['live_season_identifier']['eu']

def get_single_class(lb, season = str(get_current_season()), mode = "hardcore"):
    
    # récupération du flux en fonction de la commande
    url = f'https://assets.maxroll.gg/leaderboards/s{season}-eu-rift-{mode}-{lb}.json'
    response = requests.get(url)
    json_data = json.loads(response.content)
    data = json_data['data']
    clan_rank = 0
    best_run = f" 1er EU: GR{data[0]['rift_data']['grlvl']} en {data[0]['rift_data']['time']}"
    #```fix ``` = coloration jaune du §
    res = f"```fix\n>> CLASSEMENT {mode.upper()} {lb.upper()} S{season} <<\n"
    res = res + f"> {best_run}\n```"
    for run in data:
        if 'ctag' in run['player_data'][0]:
            if run['player_data'][0]['ctag'] == "BriT" and \
            run['player_data'][0]['cname'] == "BriTon" and \
            clan_rank < 5:
                clan_rank += 1
                res = res + f"\n#{clan_rank} : **{run['player_data'][0]['btag']}** \
p{run['player_data'][0]['plvl']} \
-> **GR{run['rift_data']['grlvl']}** \
en {run['rift_data']['time']}"
    return res

def get_teams(lb, season = str(get_current_season()), mode = "hardcore"):

    # récupération du flux en fonction de la commande
    url = f'https://assets.maxroll.gg/leaderboards/s{season}-eu-rift-{mode}-{lb}.json'
    response = requests.get(url)
    json_data = json.loads(response.content)
    data = json_data['data']

    # Parsing du #1er run EU
    best_classes = ""
    for player in data[0]['player_data']:
        best_classes = best_classes + f"[{player['class']}]"
    best_run = f" 1ers EU: {best_classes} GR{data[0]['rift_data']['grlvl']} en {data[0]['rift_data']['time']}"
    #```fix ``` = coloration jaune du §
    res = "```fix\n"
    res = res + f">> CLASSEMENT {mode.upper()} {lb.upper()} S{season} <<\n"
    res = res + f"> {best_run}\n```"
    return res + "\n*Top BriTs prochainement*"