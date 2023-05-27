import json

stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}

with open("sample.json", "w") as f:
    json.dump(stocks, f, indent=4)