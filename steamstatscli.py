# steam api key:BC4BDB9BD96C4BC0D28098C3B9D7A84C
# steamid64: 76561198158933598
import requests
url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key=BC4BDB9BD96C4BC0D28098C3B9D7A84C&steamid=76561198158933598&format=json&include_appinfo=true"

def show_all_games():
    for game in data["games"]:
        print(f"{game['name']}: {game['playtime_forever']} minutes")

played_count = 0
total_minutes = 0
response = requests.get(url)

#print(response.status_code)

data = response.json()["response"]

for game in data["games"]:
    if game["playtime_forever"] > 0:
        played_count += 1
        total_minutes += game["playtime_forever"]
        
        
total_hours = total_minutes / 60
shorten_hours = round(total_hours, 3)
sorted_games = sorted(data["games"], key=lambda g: g["playtime_forever"], reverse=True)
top_ten = sorted_games[:10]

def show_top_ten():
    for games in top_ten:
        print(f"{games['name']}: {round(games['playtime_forever'] / 60, 3)}  hours")
def show_summary():
    print(f"you have played {played_count} out of {data['game_count']} games")
    print(f"in total you have played {shorten_hours} hours or {total_minutes} minutes")

while True:
    choice = input("view: [1] summary [2] 10 most Played [3] all games [4] quit >> ")
    if choice == "1":
        show_summary()
    elif choice == "2":
        show_top_ten()
    elif choice == "3":
        show_all_games()
    elif choice == "4":
        break
    else:
        print("invalid")
        continue
    
    