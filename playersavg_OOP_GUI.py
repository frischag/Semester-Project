import requests
import nba_api_links
import utils
from tkinter import *
from tkinter.ttk import *

# ex. run: Player ID 237 and season 2016 accesses
# https://www.balldontlie.io/api/v1/season_averages?season=2016&player_ids[]=237

class NBA:
    
    def __init__(self):
        self.root = Tk()
        self.root.title("NBA Season Averages")
        self.root.geometry("330x325")
        self.root.iconbitmap("ball.ico")
        # Call methods to create frames and widgets
        self.create_frames()
        self.create_widgets()
        # Start program main loop
        mainloop()

#--------------------------GET PLAYER--------------------------#
    def get_player(self, *args):
        try:
            # Get player ID and season
            player = self.player_entry.get()
            year = self.year_entry.get()

            # Build request parameters
            # These are added on to the URL to make the complete request
            query_string = {
                "player_ids[]": player,
                "season": year
            }

            # Get the API JSON data as a Python JSON object
            response = requests.get(
                nba_api_links.SEASON_AVERAGES_URL,
                params=query_string
            )

            # Load JSON response into a weather dictionary
            player_data = response.json()

            # Get data for games played, mpg, pts, rebs,
            # and ast averages.
            self.games = player_data.get(
                "data")[0].get("games_played")
            self.mins = player_data.get(
                "data")[0].get("min")
            self.pts = player_data.get(
                "data")[0].get("pts")
            self.reb = player_data.get(
                "data")[0].get("reb")
            self.ast = player_data.get(
                "data")[0].get("ast")

            # Call display player method
            self.display_player()
        except:
            print("Sorry, there was a problem connecting.")

#--------------------------DISPLAY PLAYER--------------------------#
    def display_player(self):
        # Set the player info in the value labels
        print()
        self.lbl_games_value.configure(text=f"{self.games}")
        self.lbl_min_value.configure(text=f"{self.mins}")
        self.lbl_pts_value.configure(text=f"{self.pts}")
        self.lbl_rebs_value.configure(text=f"{self.reb}")
        self.lbl_asts_value.configure(text=f"{self.ast}")

        # Set focus to year entry for next year
        # Set this way to look at multiple seasons from one player,
        # can be changed to player entry depending on search needs
        self.year_entry.focus_set()
        # Select text in the year entry for next entry
        self.year_entry.select_range(0, END)

#-------------------------CREATE FRAMES-------------------------#
    def create_frames(self):
        self.title_frame = Frame(self.root, relief=FLAT)
        self.entry_frame = LabelFrame(
            self.root, text="Player and Season Info", relief=GROOVE)
        self.output_frame = LabelFrame(
            self.root, text="Results", relief=GROOVE)

        self.title_frame.pack(fill=X)
        self.entry_frame.pack(fill=X)
        self.output_frame.pack(fill=X)

        self.title_frame.pack_propagate(False)
        self.entry_frame.pack_propagate(False)
        self.output_frame.pack_propagate(False)

#-------------------------CREATE WIDGETS-------------------------#
    def create_widgets(self):
        # Create entry widgets and set initial focus to player entry
        self.player_entry = Entry(self.entry_frame, width=33)
        self.player_entry.focus_set()
        self.year_entry = Entry(self.entry_frame, width=33)

        # Create button to get info based on player ID and season
        self.btn_results = Button(
            self.entry_frame,
            text="Get Results",
            command=self.get_player
        )

        # Create description labels
        self.lbl_app_title = Label(self.title_frame, text="Find a players season averages",
                                       font=("Courier", 13, "bold"))
        self.lbl_player = Label(self.entry_frame, text="Enter Player ID:")
        self.lbl_year = Label(self.entry_frame, text="Enter Season:")
        self.lbl_games = Label(self.output_frame, text="Games Played:")
        self.lbl_min = Label(self.output_frame, text="Minutes/Game:")
        self.lbl_pts = Label(self.output_frame, text="Points/Game:")
        self.lbl_reb = Label(self.output_frame, text="Rebounds/Game:")
        self.lbl_ast = Label(self.output_frame, text="Assists/Game:")

        # Create value display labels
        self.lbl_games_value = Label(
            self.output_frame, width=31, anchor=W, relief=GROOVE)
        self.lbl_min_value = Label(
            self.output_frame, width=31, anchor=W, relief=GROOVE)
        self.lbl_pts_value = Label(
            self.output_frame, width=31, anchor=W, relief=GROOVE)
        self.lbl_rebs_value = Label(
            self.output_frame, width=31, anchor=W, relief=GROOVE)
        self.lbl_asts_value = Label(
            self.output_frame, width=31, anchor=W, relief=GROOVE)

        # Grid the widgets
        self.lbl_app_title.grid(row=0, columnspan=2)

        self.lbl_player.grid(row=1, column=0, sticky=E)
        self.player_entry.grid(row=1, column=1, sticky=W)
        self.lbl_year.grid(row=2, column=0, sticky=E)
        self.year_entry.grid(row=2, column=1, sticky=W)
        self.btn_results.grid(row=3, columnspan=2)

        self.lbl_games.grid(row=5, column=0, sticky=W)
        self.lbl_games_value.grid(row=5, column=1, sticky=W)

        self.lbl_min.grid(row=6, column=0, sticky=W)
        self.lbl_min_value.grid(row=6, column=1, sticky=W)

        self.lbl_pts.grid(row=7, column=0, sticky=W)
        self.lbl_pts_value.grid(row=7, column=1, sticky=W)

        self.lbl_reb.grid(row=8, column=0, sticky=W)
        self.lbl_rebs_value.grid(row=8, column=1, sticky=W)

        self.lbl_ast.grid(row=9, column=0, sticky=W)
        self.lbl_asts_value.grid(row=9, column=1, sticky=W)

        # Set padding for all widgets in window
        self.title_frame.pack_configure(padx=10, pady=(10, 0))
        self.entry_frame.pack_configure(padx=10, pady=(10, 0))
        self.output_frame.pack(padx=10, pady=10)
        for widget in self.entry_frame.winfo_children():
            widget.grid_configure(padx=3, pady=3)
        for widget in self.output_frame.winfo_children():
            widget.grid_configure(padx=3, pady=3)
        # Set focus to the player entry box for the next location
        self.player_entry.focus_set()

        # The enter key will activate the calculate method
        self.root.bind('<Return>', self.get_player)


nba = NBA()
