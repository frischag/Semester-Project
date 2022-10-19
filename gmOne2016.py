import requests
import os

IS_DEBUGGING = True

URL = "https://www.balldontlie.io/api/v1/games/1"

def main():
    response = requests.get(URL)

    if(response.status_code == 200):

        data = response.json()

        if(IS_DEBUGGING == True):

            # Display the status code
            print(
                f"\nThe status code for this API request is {response.status_code} \n")

            # Display the raw JSON data from the API
            print("The raw data from the BallDontLieAPI:")
            print(response.text)

            # Print the Python dictionary
            print(f"\nThe JSON data converted to a Python dictionary:")
            print(data)

        # Print the data using the dictionary created from the API JSON data
        print(f"{data.get('date')}")
        print(f"\n{data.get('home_team').get('full_name')}: {data.get('home_team_score')}")
        print(f"vs.")
        print(f"{data.get('visitor_team').get('full_name')}: {data.get('visitor_team_score')} ")
    else:
        print("API unavailable")

# Menu loop
while True:
    # Clear the screen
    os.system("cls" if os.name == "nt" else "clear")
    # Call the main method to get a new Dictum
    main()
    # Display menu choices
    answer = input(
        "\nSee another game? ([y] or [Enter] to quit)? ")
    # Exit program
    if answer != "y":
        break
