import time

def introduction():
    print("Welcome to my Text Adventure Game!")
    time.sleep(1)
    print("You are about to enter a dangerous cave filled with unknown encounters.")
    time.sleep(1)
    print("The objective is to get through the underground cave and find the treasure.")
    time.sleep(1)

def make_choice(question, options):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def cave_entry():
    print("You enter the cave and encounter a fork in the path.")
    time.sleep(1)
    choice = make_choice("Which path will you take?", ["Go left", "Go right"])

    if choice == 1:
        print("You chose to go left. As you walk, you find a key.")
        time.sleep(1)
        return True
    else:
        print("You chose to go right. This seemed to be a safe path to take.")
        time.sleep(1)
        print("You proceed with caution.")
        return False

def sleeping_goblin(has_key):
    print("You reach the next room to find a sleeping goblin")
    time.sleep(1)
    choice = make_choice("Do you wake the goblin or sneak past it?", ["Wake Goblin", "Sneak Past"])

    if choice == 1:
        print("You chose to wake the goblin. The Goblin wakes in anger and attacks you.")
        choice2 = make_choice("Do you punch first or block his attack?", ["Punch Goblin", "Block Attack"])
        time.sleep(1)
        if choice2 == 1:
            print("You chose to punch the Goblin first.")
            if has_key:
                print("You punched the Goblin first and stunned him. But your key fell out in the process.")
                time.sleep(1)
                return False
            else:
                print("You punched the Goblin first and succeeded. The Goblin is knocked out and you find a Key on his belt.")
                time.sleep(1)
                return True
        else:
            print("You chose to Block the Goblins attack.")
            if has_key:
                print("You successfully blocked the Goblins attack and ran away.")
                time.sleep(1)
                return True
            else:
                print("You successfully blocked the Goblins attack and ran away.")
    else:
        if has_key:
            print("You chose to sneak past the goblin. You encounter a locked door.")
            time.sleep(1)
            print("You need a key to proceed.")
            return True
        else:
            print("You chose to sneak past the goblin. You encounter a locked door.")
            time.sleep(1)
            print("You need a key to proceed.")
            return False

def treasure_room(has_key):
    print("You reach the treasure room, where a chest awaits.")
    time.sleep(1)

    if has_key:
        print("You use the key to open the chest.")
        time.sleep(1)
        print("Congratulations! You found the treasure.")
    else:
        print("The chest is locked. You need to find a key to open it.")

def play_game():
    introduction()

    # Cave Entry
    key_found = cave_entry()
   
    # Encounter Sleeping Goblin
    key_found = sleeping_goblin(key_found)

    # Treasure Room
    treasure_room(key_found)

if __name__ == "__main__":
    play_game()
