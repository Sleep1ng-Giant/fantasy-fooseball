import requests
import json
from collections import defaultdict

def get_player_data():
    """
    Fetches player data from the Sleeper API.

    This function sends a GET request to the Sleeper API to retrieve player data in JSON format,
    which contains information about all NFL players. The data is returned as a dictionary where
    each key is a player's ID, and the corresponding value is a dictionary of player attributes.

    Returns:
        dict: A dictionary containing player data for all NFL players.

    Example:
        players = get_player_data()
        # players is a dictionary like:
        # {
        #     "12345": {"full_name": "John Doe", "team": "DAL", "position": "QB", ...},
        #     "67890": {"full_name": "Jane Smith", "team": "NE", "position": "WR", ...},
        # }
    """
    url = "https://api.sleeper.app/v1/players/nfl"
    response = requests.get(url)
    return response.json()

def filter_and_group_players(players):
    """
    Filters and groups active offensive players by their respective teams.

    This function processes player data to include only active players with valid offensive positions
    (QB, WR, RB, TE, K) and groups them by their team. It extracts relevant player information like
    name, team, status, and position, and organizes players into a dictionary keyed by their team name.

    Args:
        players (dict): A dictionary containing player data for all NFL players.

    Returns:
        dict: A dictionary where each key is a team name, and the corresponding value is a list of
              player data dictionaries representing active offensive players on that team.

    Example:
        grouped_players = filter_and_group_players(players)
        # {
        #     "DAL": [{"player_id": "12345", "full_name": "John Doe", "team": "DAL", ...}],
        #     "NE": [{"player_id": "67890", "full_name": "Jane Smith", "team": "NE", ...}],
        # }
    """
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
    """
    Saves player data to a JSON file in a prettified (indented) format.

    This function takes the filtered and grouped player data and saves it to a JSON file
    with indentation for readability.

    Args:
        player_data (dict): The player data to be saved in JSON format.
        filename (str): The name of the file to save the data to. Defaults to 'players_pretty.json'.

    Example:
        save_prettified_json(grouped_players, 'players_pretty.json')
        # This will save the grouped players into 'players_pretty.json'.
    """
    with open(filename, 'w') as file:
        json.dump(player_data, file, indent=4)

    print(f"Player data saved to {filename} in prettified format.")

# Main execution
players = get_player_data()
grouped_players = filter_and_group_players(players)
save_prettified_json(grouped_players, 'players_pretty.json')
    
