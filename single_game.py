"""
ex: 'https://www.balldontlie.io/api/v1/stats?season[]=2018&player_ids[]=237&game_ids[]=15498'
     is link for playerid:237, season:2018, game:15498
            
"""

import requests
import nba_api_links
import utils


class NBA:
    def __init__(self):
        print(utils.title("NBA Game Search"))

    def get_player(self):
        self.playerid = input("Enter player ID: ")
        # self.dateid = input("Enter a date: ")
        self.seasonid = input("Enter season: ")
        self.gameid = input("Enter game ID: ")
        self.player = f"{self.playerid}"
        # self.date = f"{self.dateid}"
        self.season = f"{self.seasonid}"
        self.game = f"{self.gameid}"

    def stat_parameters(self):
        # Set to true to print raw data
        try:
            query_string = {
                "season[]": self.season,
                "player_ids[]": self.player,
                "game_ids[]": self.game
                #"dates[]": self.date
            }
            
            response = requests.get(
                nba_api_links.PLAYER_STATS_URL,
                params=query_string
            )
            if(response.status_code == 200):

                self.player_data = response.json()
                print("Successful")
            else:
                print("Invalid request")
                self.get_player()
            
            self.points = self.player_data.get(
                "data")[0].get("pts")
            self.rebounds = self.player_data.get(
                "data")[0].get("reb")
            self.assists = self.player_data.get(
                "data")[0].get("ast")
            self.fgm = self.player_data.get(
                "data")[0].get("fgm")
            self.fga = self.player_data.get(
                "data")[0].get("fga")
            self.oreb = self.player_data.get(
                "data")[0].get("oreb")
            self.turnovers = self.player_data.get(
                "data")[0].get("turnover")
            self.firstname = self.player_data.get(
                "data")[0].get("player").get("first_name")
            self.surname = self.player_data.get(
                "data")[0].get("player").get("last_name")
            
        
        except:
            print("Sorry, connection problem.")
       

    def calculate_oe(self):
        self.oe = (self.fgm + self.assists) / (self.fga - self.oreb + self.assists + self.turnovers)
        
    def display_player(self):
        print(f"Name: {self.firstname} {self.surname}")
        print(f"Points: {self.points}")
        print(f"Rebounds: {self.rebounds}")
        print(f"Assists: {self.assists}")
        print(f"Efficiency rating: {self.oe:.2f}%")

still_running = 'y'

while True:
    nba = NBA()
    nba.get_player()
    nba.stat_parameters()
    nba.calculate_oe()
    nba.display_player()
    still_running = input("Search again? y for yes, any other key to exit: ")
    if still_running != 'y':
        print("Thanks for visiting!")
        break
            

