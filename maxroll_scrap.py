import requests
import json

def get_current_season():
    url = 'https://assets.maxroll.gg/leaderboards/leaderboard_index.json'
    response = requests.get(url)
    data = json.loads(response.content)
    return data['season']['live_season_identifier']['eu']

# TODO : nommage de la fonction à affiner en fonction du parsing réalisé côté bot
def get_single_class(lb):
    # TODO : placeholders à parser en fonction du mot clef
    mode = "hardcore"
    season = str(get_current_season())

    # récupération du flux en fonction de la recherche
    url = f'https://assets.maxroll.gg/leaderboards/s{season}-eu-rift-{mode}-{lb}.json'
    response = requests.get(url)
    json_data = json.loads(response.content)
    data = json_data['data']
    clan_rank = 0
    best_run = f"(1er EU: GR{data[0]['rift_data']['grlvl']} en {data[0]['rift_data']['time']})"
    res = f">> CLASSEMENT {mode.upper()} {lb.upper()} S{season} {best_run} <<\n"
    for run in data:
        if 'ctag' in run['player_data'][0]:
            if run['player_data'][0]['ctag'] == "BriT" and \
            run['player_data'][0]['cname'] == "BriTon" and \
            clan_rank < 5:
                clan_rank += 1
                res = res + f"\n#{clan_rank} : {run['player_data'][0]['btag']} \
p{run['player_data'][0]['plvl']} \
-> GR{run['rift_data']['grlvl']} \
en {run['rift_data']['time']}"
    return res