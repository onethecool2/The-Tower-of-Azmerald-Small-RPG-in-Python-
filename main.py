from functions import selection, movement_tutorial
from savefile import create_save, save_access, start_over
from tiles import tile_generation, tile_read
from settings import settings_access
position, inventory, statistics, name, character_type, tutorial = save_access()
difficulty, auto_examine = settings_access()
game_start = "0"
secret3 = []
playing_game = False
#################################################


print("The Tower of Azmerald")
print("By: LetZoneG")
print()
input("Press enter to continue... ^")
print("\n" * 20)
if tutorial == 0:
    difficulty = 0
    print("Whenever you see and arrow like this: ^")
    input("Press enter ^")
    print("\n" * 20)
    print("Welcome to the world of Azmerald!")
    secret = input("A magical world of mystery ^")
    print("\nThe first step to starting your adventure is")
    input("selecting your character type ^")
    print("\n" * 20 + "Please select on of the following:")
    print("1. Knight: Average in all")
    print("2. Witch: Has lots of mana but consumes it quite a bit faster, average in health, weak base attack")
    print("3. Troll: Has a lot of strength, has barely any mana, average health")
    print("4. Healer: Has a lot of health, average mana levels, weak base attack")
    if secret == "DaemonBorn":
        print("S1. Daemon: High in all")
    if secret == "VillageBorn":
        print("S2. Villager: Low in all")
    if secret == "DaemonVillager":
        print("S1. Daemon: High in all")
        print("S2. Villager: Low in all")
    character_input = input("Please select the character of your choosing: ")
    if character_input.upper() == "KNIGHT" or character_input == "1":
        character_type = "knight"
        statistics = [50, 5, 50, 1, 0]
    elif character_input.upper() == "WITCH" or character_input == "2":
        character_type = "witch"
        statistics = [50, 10, 20, 1, 0]
    elif character_input.upper() == "TROLL" or character_input == "3":
        character_type = "troll"
        statistics = [50, 2, 100, 1, 0]
    elif character_input.upper() == "HEALER" or character_input == "4":
        character_type = "healer"
        statistics = [100, 5, 20, 1, 0]
    elif character_input.upper() == "DAEMON" or character_input.upper() == "S1":
        if secret == "DaemonBorn" or secret == "DaemonVillager":
            character_type = "daemon"
            statistics = [100, 10, 100, 1, 0]
    elif character_input.upper() == "VILLAGER" or character_input.upper() == "S2":
        if secret == "VillageBorn" or secret == "DaemonVillager":
            character_type = "villager"
            statistics = [20, 0, 20, 1, 0]
    else:
        character_type = "satyr"
        statistics = [50, 5, 50, 1, 0]
    print("Welcome to Azmerald then young " + character_type + "!")
    name = input("So now, what is your name? ")
    if name == "":
        name = "Juan"
    input("So you are " + name + " the " + character_type + "! ^")
    input("Well then, let's get moving then. ^")
    print("\n" * 20)
    tutorial = movement_tutorial()
    print("What difficulty would you like to play at?")
    print("1. Easy")
    print("2. Normal")
    print("3. Hard")
    while difficulty == 0:
        diff_selection = input()
        if diff_selection == "1":
            difficulty = 1
            print("Difficulty is now Easy")
        elif diff_selection == "2":
            difficulty = 2
            print("Difficulty is now Normal")
        elif diff_selection == "3":
            difficulty = 3
            print("Difficulty is now Hard")
    statistics[0] += int(0.25 * (difficulty * statistics[0]))
    statistics[1] += int(0.25 * (difficulty * statistics[1]))
    statistics[2] += float(0.25 * (difficulty * statistics[2]))
    auto_selection = input("Would  you like to turn on auto-examine? ")
    if auto_selection == "y" or auto_selection == "yes":
        print("Auto-examine turned on")
        auto_examine = 1
        input("You can change this from the main menu upon restart. ^")
    else:
        print("Auto-examine turned off")
        auto_examine = 0
        input("You can change this from the main menu upon restart. ^")
    tile_generation()
    floor0, floor1, floor2, floor3, floor4 = tile_read()
    create_save(position, inventory, statistics, name, character_type, tutorial, floor0, floor1, floor2, floor3, floor4, difficulty, auto_examine)
    playing_game = True
    print("\n" * 20)
else:
    secret2 = input("Welcome back to Azmerald, " + name + " the " + character_type + "! ^")
    if secret2 == "^^vv<><>BA+":
        statistics[0] += 1000
        statistics[1] += 100
        statistics[2] += 50
    while game_start == "0":
        print("What would you like to do?")
        print("1. Continue game from last save")
        print("2. Clear save and start over")
        print("3. Settings")
        print("4. Change name")
        print("5. Exit game")
        game_start = input()
        if game_start == "1":
            input("Alright, let's begin then! ^")
            print("\n" * 20)
            playing_game = True
        elif game_start == "2":
            confirmation_start_over = input("Are you sure you want to start over? ")
            if confirmation_start_over.lower() == "yes" or confirmation_start_over.lower() == "y":
                input("Starting over ^")
                start_over()
                quit()
            else:
                input("Cancelling... ^")
                game_start = "0"
                print("\n" * 20)
        elif game_start == "3":
            if auto_examine == 0:
                examine = input("Would you like to turn on auto-examine? ")
                if examine.lower() == "y" or examine.lower() == "yes":
                    auto_examine = 1
                else:
                    game_start = "0"
            elif auto_examine == 1:
                examine = input("Would you like to turn off auto-examine? ")
                if examine.lower() == "y" or examine.lower() == "yes":
                    auto_examine = 0
                else:
                    game_start = "0"
            print("\n" * 20)
        elif game_start == "4":
            confirmation_name = input("Are you sure you want to change your name? ")
            if confirmation_name.lower() == "yes" or confirmation_name.lower() == "y":
                new_name = input("What's your new name then? ")
                confirmation_new_name = input("Are you sure you want your new name to be " + new_name + "? ")
                if confirmation_new_name.lower() == "yes" or confirmation_new_name.lower() == "y":
                    name = new_name
                else:
                    input("Cancelling... ^")
            else:
                input("Cancelling... ^")
            print("\n" * 20)
            game_start = "0"
        elif game_start == "5":
            input("Exiting game... ^")
            quit()
        else:
            print("\n" * 20)
            game_start = "0"

while playing_game:
    selection(position, inventory, statistics, name, character_type, tutorial, secret3, difficulty, auto_examine)
