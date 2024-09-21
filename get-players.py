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
#save_players_to_file(players, 'my_players.json')

def save_prettified_json(player_data, filename='players_pretty.json'):
    with open(filename, 'w') as file:
        # Save the JSON with an indent of 4 for pretty formatting
        json.dump(player_data, file, indent=4)

    print(f"Player data saved to {filename} in prettified format.")
    
player_data = get_player_data()  
save_prettified_json(player_data, 'players_pretty.json')
    