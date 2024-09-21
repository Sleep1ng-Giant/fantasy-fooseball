import requests
import json

def get_player_data():
    url = "https://api.sleeper.app/v1/players/nfl"
    response = requests.get(url)
    return response.json()

def save_players_to_file(players, filename='players.json'):
    with open(filename, 'w') as f:
        json.dump(players, f)
        
        
players = get_player_data()
save_players_to_file(players, 'my_players.json')

