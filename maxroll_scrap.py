import requests
import json

def get_current_season():
    url = 'https://assets.maxroll.gg/leaderboards/leaderboard_index.json'
    response = requests.get(url)
    data = json.loads(response.content)
    return data['season']['live_season_identifier']['eu']