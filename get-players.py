import requests
import json
from collections import defaultdict

def get_player_data():
    url = "https://api.sleeper.app/v1/players/nfl"
    response = requests.get(url)
    return response.json()

def filter_and_group_players(players):
    valid_positions = {"QB", "WR", "RB", "TE", "K"}
    grouped_players = defaultdict(list)

    for player_id, player_info in players.items():
        # Check for valid depth_chart_position and active status
        if player_info.get('depth_chart_position') and player_info.get('active'):
            # Extract relevant information
            player_data = {
                "player_id": player_id,
                "search_first_name": player_info.get("search_first_name"),
                "search_last_name": player_info.get("search_last_name"),
                "metadata": {"rookie_year": player_info.get("metadata", {}).get("rookie_year")},
                "active": player_info.get("active"),
                "injury_status": player_info.get("injury_status"),
                "status": player_info.get("status"),
                "age": player_info.get("age"),
                "team": player_info.get("team"),
                "full_name": player_info.get("full_name")
            }
            grouped_players[player_info["team"]].append(player_data)

    return grouped_players

def save_prettified_json(player_data, filename='players_pretty.json'):
    with open(filename, 'w') as file:
        json.dump(player_data, file, indent=4)

    print(f"Player data saved to {filename} in prettified format.")

# Main execution
players = get_player_data()
grouped_players = filter_and_group_players(players)
save_prettified_json(grouped_players, 'players_pretty.json')
    