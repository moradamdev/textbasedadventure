# Adam Morales
# Text Based Game

# Dictionary of all rooms and items
rooms = {
    'Town Hall': {'West': 'Church'},
    'Church': {'East': 'Town Hall', 'South': 'Subway', 'item': 'Cross'},
    'Subway': {'West': 'Pizzeria', 'East': 'Hospital', 'South': 'Tailor', 'North': 'Church', 'item': 'Metro Card'},
    'Pizzeria': {'East': 'Subway', 'item': 'Garlic'},
    'Tailor': {'North': 'Subway', 'East': 'Bar', 'item': 'Turtle Neck'},
    'Bar': {'West': 'Tailor', 'item': 'Potion'},
    'Hospital': {'West': 'Subway', 'North': 'Central Park', 'item': 'Blood Vial'},
    'Central Park': {'item': 'Dracula'}
}
def show_instructions():
   #Print a main menu and the commands
   print("Dracula Text Adventure Game")
   print("Collect 6 items to win the game, or be killed by Dracula")
   print("Move commands: go South, go North, go East, go West")
   print("Add to Inventory: get 'item name'")
   print("Type 'Instructions' to show the instructions again")
   print("----------------------------------------------------------")

# Set the default current room to the Great Hall
currentRoom = 'Town Hall'
possibleCommands = ['go East', 'go West', 'go South', 'go North']
dir = ''
items = []

# Loop until current room is exit
show_instructions()
while currentRoom != 'Central Park':
    print("You are currently in:", currentRoom)
    print("Inventory", items)
    if 'item' in rooms[currentRoom] and rooms[currentRoom]['item'] not in items:
        print("You see a", rooms[currentRoom]['item'])
    command = input("What would you like to do?: ")

    # Check if the command is valid to avoid any errors and not run unnecessary code
    if command in possibleCommands:
        # Split the command and choose the second item in list since command is 'go Direction'
        dir = command.split()[1]
        if dir in rooms[currentRoom]:
            #Ex. if 'South' in rooms['Great Hall'] then change the current room, else 'Can't go that way'
            currentRoom = rooms[currentRoom][dir]
            print('You move to the', currentRoom)
        else:
            print("You can't go that way")
    elif command.split()[0] == 'get':
        tempItem = " ".join(command.split()[1:])
        if tempItem == rooms[currentRoom]['item']:
            if(command.split()[1] not in items):
                items.append(tempItem)
                print("Added item to inventory")
            else:
                print("This item is already in your inventory")
        else:
            print('This item is not in this room')
    elif command.upper() == "INSTRUCTIONS":
        show_instructions()
    print("----------------------------------------------------------")

print("Dracula stands before you menancingly.")
if(len(items) < 6):
    print("You don't have all the items needed to defeat Dracula. He slays you and you fail to save NYC.")
    print("Game Over.")
else:
    print("You beat Dracula using all the items you've gathered and are crowned the hero of NYC.")
    print("You Win!")
