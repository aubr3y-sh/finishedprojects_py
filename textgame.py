current_room = "foyer"
room_description = "the air is heavy and still"
player_health = 100  
game_running = True
inventory = []

print(f"your health is {player_health}")
print(f"you are in {current_room} , {room_description}")

rooms = {
    "foyer": {
        "description": "the air is heavy and still",
        "exits": {"north": "stairs", "east": "dining hall", "west": "courtyard"}
    },
    "courtyard": {
        "description": "dead vines wrap the outside walls and a large tree grows from cracked tiles",
        "exits": {"east": "foyer"},
        "item": "rusty key"
    },
    "dining hall": {
        "description": "a large table sits wretchedly with the remains of a feast decaying atop it",
        "exits": {"west": "foyer", "north": "courtyard"},
        "item": "new key"
    },
    "stairs": {
        "description": "you walk up a wide marble staircase that branches off to the west and east",
        "exits": {"west": "courtyard", "east": "dining hall"}
    },
}

def describe_room(room_name):
    print(rooms[room_name]["description"])

while game_running:

    direction = input("where will you go? [north, east, south, west, quit, look, take] ")
    if direction in rooms[current_room]["exits"]:
        current_room = rooms[current_room]["exits"][direction]
        print(f"you go {direction}")
        describe_room(current_room)
    elif current_room == "foyer" and direction == "south":
        if "rusty key" in inventory and "new key" in inventory:
            print("you have escaped the chateau")
            break
        else:
            print("the door is locked")
            continue
    elif direction == "look":
        print(f"you are in the {current_room} and have {inventory}")
    elif direction == "take":
        if "item" in rooms[current_room]:
            item = rooms[current_room]["item"]
            inventory.append(item)
            print(f"you added {item} to your inventory")
            del rooms[current_room]["item"]
            continue
        else:
            print("there is nothing to pick up")
            continue
    elif direction == "quit":
        break
    else:
        print("you cannot go that way")
        player_health -= 15
        if player_health <= 0: 
            print("You Died...")
            break
        print(f"your health is {player_health}")
        continue