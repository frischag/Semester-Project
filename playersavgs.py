import requests
import nba_api_links
import utils

# ex. run: Player ID 237 and season 2016 accesses
# https://www.balldontlie.io/api/v1/season_averages?season=2016&player_ids[]=237
class NBA:
    def __init__(self):
        print(utils.title("NBA Season Averages"))

    def get_player(self):
        self.playerid = input("Enter player ID: ")
        self.yearid = input("Enter year: ")
        self.player = f"{self.playerid}"
        self.year = f"{self.yearid}"

    def player_parameters(self):
        query_string = {
            "player_ids[]": self.player,
            "season": self.year
        }

        response = requests.get(
            nba_api_links.SEASON_AVERAGES_URL,
            params=query_string
        )

        self.player_data = response.json()

        self.games = self.player_data.get(
            "data")[0].get("games_played")
        self.pts = self.player_data.get(
            "data")[0].get("pts")
        self.reb = self.player_data.get(
            "data")[0].get("reb")
        self.ast = self.player_data.get(
            "data")[0].get("ast")
        
        

    def display_player(self):
        print()
        print(f"Games played:      {self.games}")
        print(f"Points per game:   {self.pts}")
        print(f"Rebounds per game: {self.reb}")
        print(f"Assists per game:  {self.ast}")

nba = NBA()
nba.get_player()
nba.player_parameters()
nba.display_player()
