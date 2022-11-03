import json
import requests

teams = requests.get(f'https://www.balldontlie.io/api/v1/teams')
teamIds = teams.json()

# Uncomment below for raw data
# print(json.dumps(teamIds, indent=4))

for d in teamIds['data']:
    print(d['id'],".", d['full_name'])
    # Uncomment below as needed for additional team info
    # print("\nAbbreviation:",d['abbreviation'])
    # print("        City:",d['city'])
    # print("  Conference:",d['conference'])
    # print("    Division:",d['division'])
    # print("        Name:",d['name'])
    print('-'*80)
    
