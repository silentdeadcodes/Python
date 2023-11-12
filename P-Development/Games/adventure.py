# Created using GPT

import time

class Player:
    def __init__(self):
        self.inventory = []

def introduction():
    print("Welcome to the Complex Adventure Game!")
    time.sleep(1)
    print("You wake up in a mysterious castle. Your goal is to find the treasure and escape.")

def choose_action():
    print("Choose your action:")
    print("1. Explore the room.")
    print("2. Check your inventory.")
    print("3. Quit the game.")
    
    return input("Enter 1, 2, or 3: ")

def explore_room(player):
    print("You explore the room and find:")
    time.sleep(1)

    # Random events or items can be added here
    event = "You find a key on the table."
    print(event)
    if "key" not in player.inventory:
        player.inventory.append("key")

def check_inventory(player):
    print("Your inventory:", player.inventory)

# test for org game

def main():
    player = Player()
    introduction()

    while True:
        action = choose_action()

        if action == '1':
            explore_room(player)
        elif action == '2':
            check_inventory(player)
        elif action == '3':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
call = 'kill'
print(call + ": 13 11 15")
