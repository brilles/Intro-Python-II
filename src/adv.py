from room import Room
from player import Player
from item import Item

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
"North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Declare all the items
items = {
    "sword": Item("Sword", "The mighty sword"),
    "helmet": Item("Helmet", "The magical helmet"),
    "armour": Item("Armour", "The protective armour"),
    "gem": Item("Gem", "The wizard gem"),
    "scroll": Item("Scroll", "The super scroll"),
    "treasure": Item("Treasure", "The pot of gold")
}

# Link rooms together
room['outside'].n_to = room['foyer'] 
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Link items to rooms
room['outside'].items = [items['sword']]
room['foyer'].items = [items['helmet']]
room['narrow'].items = [items['armour']]
room['overlook'].items = [items['gem']]
room['treasure'].items = [items['scroll'], items['treasure']]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Player1", room['outside'])

while True: 
    # Prints the player's name
    print(player.name)
    # Prints the current room name
    print(player.current_room.name)

    # Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)

    # checking for items
    try: 
        player.current_room.items[0]
                # Prints the items in the room
        print('Items: ')
        for i in player.current_room.items:
            print(f"{i.name} - '{i.description}'")
    except:
        print("No items here, look elsewhere")

    try:
        # Waits for user input and decides what to do.
        cmd = input("\nEnter a command: ").lower().split()

        if len(cmd) == 1:
            # quit game
            if cmd[0][0] == "q":
                print("Game ended")
                break
            #show inventory
            if cmd[0][0] == "i":
                if len(player.items) == 0:
                    print("You don't have any items!")
                else:
                    print('Your items: ')
                for i in player.items:
                    print(f"{i.name} - '{i.description}'")
            # check the input direction is valid
            attribute = f'{cmd[0][0]}_to'
            if hasattr(player.current_room, attribute):
                # set the new room
                player.current_room =  getattr(player.current_room, attribute)
            else:
                print("Wrong way! Try again, hint: enter n, s, e, w")
                continue
        elif len(cmd) == 2:
            # user entered a verb and object e.g "drop sword"
            if cmd[0] == "get" or cmd[0] == "take":
                # check if available
                for i in player.current_room.items:
                    if cmd[1] == i.name.lower():
                        player.current_room.items.remove(i)
                        player.items.append(i)
                        print(i.on_take())
                    else:
                        print("Item not in this room, try another")
            elif cmd[0] == "drop":
                # check if have that one, if no check it actually exist, related msgs
                if len(player.items) == 0:
                    print("You don't have any items to drop!")
                else: 
                    for i in player.items:
                        if cmd[1] == i.name.lower():
                            player.items.remove(i)
                            player.current_room.items.append(i)
                            print(i.on_drop())
                        else:
                            print("You dont have that item.")
            else:
                print("Invalid command. Please try again")
        else: 
            print("Invalid command. Please try again")
    except:
        # if nothing entered
        print("Something must be entered!")
        continue



    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
