from savefile import create_save
from tiles import tile_read, tile_write
import random


# Teaches how to play the game #
def movement_tutorial():
    print("Questions:")
    print("You'll often find yourself encountering questions like 'Do you want to take a potion?'.")
    print("These yes or no questions can be answered with 'yes' or 'y'.")
    print("Anything other than that will be recognized as 'no'.")
    input("^")
    print("You'll also encounter questions like 'Which way?' or questions with number answers.")
    print("These questions can be answered by entering the corresponding number.")
    print("Anything other than the numbers stated will exit you out of the selection or you'll be asked the same question again.")
    input("^")
    print("")
    print("Movement: ")
    print("Your position is represented by 3 coordinates:")
    input("[X (horizontal), Y (vertical), Z (current floor)] ^")
    print("\nThere are 4 floors, your goal is to get to the 4th floor and defeat The Great Dragon.")
    input("Each floor has a 4x4 area to explore as you wish. ^")
    print("\nYou will always have eight actions to take:")
    print("1. Move (A sub menu will let you choose if you want to move forward, forward, left, or right.)")
    print("2. Examine (Let's you look at what's in the space you're currently in.)")
    print("3. Statistics (Let's you look at current level, EXP amount, health, mana, and power.)")
    print("4. Inventory (Let's you look at how many of any items you have & take a potion if you want to.)")
    print("5. Map (Let's you look at where you are on the X and Y coordinates.)")
    print("6. Save Game (Saves items, health, and all information for when you come back.)")
    print("7. Tutorial (Lets you check the movement tutorial at any time.)")
    print("8. Exit Game (Let's you leave the game, make sure to save before you do so or you'll lose all your progress.)")
    input("^")
    print("")
    print("Examining:")
    print("When you examine the space you are on, one of many things can happen.")
    print("That can include: Getting a health / mana potion, getting a key, encountering stairs, or encountering an enemy.")
    print("You can only go up stairs if you have a key.")
    print("If a space has an enemy, that space will continue to have enemies on it even after you've defeated one, it's a great way to grind EXP.")
    input("^")
    print("")
    print("Battle: ")
    print("When you're in battle, you'll have 3 options to pick from.")
    print("1. Fight (Lets you do damage to the enemy) (You'll be able to power up your attack with mana.)")
    print("2. Protect (Lets you defend yourself from incoming attacks.)")
    print("3. Take Potion (Lets you use a health or mana potion to heal you or recover mana respectively.)")
    input("^")
    print("")
    print("Post-Battle: ")
    print("After every battle you'll gain EXP, it is dependant on what kind of enemy you've fought.")
    input("Additionally, you'll also get a drop which is completely random. ^")
    print("")
    print("Leveling-up: ")
    print("Once you reach certain EXP milestones, you'll level up.")
    print("Each time you level up, the milestone increases.")
    print("Leveling up isn't just to look cool but it also increases your power by 10% and thus your attacks do more damage.")
    input("^")
    print("")
    print("Getting ready for The Great Dragon:")
    print("The Great Dragon is very powerful so you'll need a lot of health and a lot of mana.")
    print("From the inventory menu you can choose to take potions.")
    print("Note that there is no limit to how much health or mana you can have so take any potions you have on you.")
    input("^")
    print("")
    print("Saving:")
    print("Always make sure to save whenever you can or else you'll lose all your progress.")
    print("Even if you don't save, the tiles you've been on will save no matter what so be careful.")
    input("^")
    print("")
    print("Settings:")
    print("Difficulty: You only get one chance to select your difficulty so choose wisely")
    print("   -There are three difficulties: Easy, Normal, and Hard (Not recommended for first play-through)")
    print("Auto-examine: automatically examines whenever you move.")
    input("You are now ready to go! ^")
    print("\n" * 20)
    tutorial = 1
    return tutorial


# Player decides what to do #
def selection(position, inventory, statistics, name, character_type, tutorial, secret3, difficulty, auto_examine):
    while statistics[4] >= int(100 + (0.2 * (statistics[3] * 100))):
        level_up(statistics)
    if secret3 == [1, 9, 8, 7]:
        freddy_fazbear(inventory, statistics, name, character_type, position, difficulty)
    floor0, floor1, floor2, floor3, floor4 = tile_read()
    print("Current position:")
    print(position)
    print("What would you like to do?")
    print("1. Move")
    print("2. Examine")
    print("3. Statistics")
    print("4. Inventory")
    print("5. Map")
    print("6. Save Game")
    print("7. Tutorial")
    print("8. Exit Game")
    selection = input()
    if selection == "1" and auto_examine == 0:
        movement(position)
    elif selection == "1" and auto_examine == 1:
        movement(position)
        examine_z(position, inventory, statistics, name, character_type, secret3, difficulty)
    elif selection == "2":
        examine_z(position, inventory, statistics, name, character_type, secret3, difficulty)
    elif selection == "3":
        print("\n")
        print("LVL: " + str(statistics[3]))
        print("EXP: " + str(int(statistics[4])) + "/" + str(int(100 + (0.2 * (statistics[3] * 100)))))
        print("Health: " + str(statistics[0]))
        print("Mana: " + str(statistics[1]))
        print("Power: " + str(statistics[2]))
        input("^")
        print("\n" * 20)
    elif selection == "4":
        take_potion = True
        while take_potion:
            print("\n" * 20)
            print("Health Potions: " + str(inventory[0]))
            print("Mana Potions: " + str(inventory[1]))
            print("Keys: " + str(inventory[2]))
            print("What kind of potion would you like to take? ")
            print("1. Health")
            print("2. Mana")
            print("3. Exit Inventory")
            which_potion = input("")
            if which_potion == "1":
                if inventory[0] >= 1:
                    inventory[0] -= 1
                    input("Consumed potion. ^")
                    statistics[0] += 50
                    print("Health increased by 50.")
                else:
                    print("You don't have any of that potion type.")
            elif which_potion == "2":
                if inventory[1] >= 1:
                    inventory[1] -= 1
                    input("Consumed potion. ^")
                    statistics[1] += 5
                    print("Mana increased by 5.")
                else:
                    print("You don't have any of that potion type.")
            else:
                break
            input("^")
        print("\n" * 20)
    elif selection == "5":
        location(position)
    elif selection == "6":
        input("Saving game... ^")
        create_save(position, inventory, statistics, name, character_type, tutorial, floor0, floor1, floor2, floor3, floor4, difficulty, auto_examine)
        input("Game saved! ^")
        print("\n" * 20)
    elif selection == "7":
        print("\n" * 20)
        movement_tutorial()
    elif selection == "8":
        save = input("Do you want to save? ")
        if save.lower() == "y" or save.lower() == "yes":
            input("Saving game... ^")
            create_save(position, inventory, statistics, name, character_type, tutorial, floor0, floor1, floor2, floor3, floor4, difficulty, auto_examine)
            input("Game saved! ^")
        input("Exiting game... ^")
        exit()


# Allows the player to move around the map in the four cardinal directions #
def movement(position):
    print("Which direction? ")
    print("1. Forward")
    print("2. Backward")
    print("3. Left")
    print("4. Right")
    selection = input()
    if selection == "1":
        if position[1] < 3:
            input("You moved forward one space. ^")
            position[1] += 1
            print("\n" * 20)
        else:
            input("You can't move forward any more.^")
            print("\n" * 20)
    elif selection == "2":
        if position[1] > 0:
            input("You moved backward one space. ^")
            position[1] -= 1
            print("\n" * 20)
        else:
            input("You can't move backward any more.^")
            print("\n" * 20)
    elif selection == "3":
        if position[0] > 0:
            input("You moved left one space. ^")
            position[0] -= 1
            print("\n" * 20)
        else:
            input("You can't move left any more.^")
            print("\n" * 20)
    elif selection == "4":
        if position[0] < 3:
            input("You moved right one space. ^")
            position[0] += 1
            print("\n" * 20)
        else:
            input("You can't move right any more.^")
            print("\n" * 20)


# Allows the player to explore the space they're currently on, cannot explore previously explored unless it's stairs #
def examine_z(position, inventory, statistics, name, character_type, secret3, difficulty):
    floor0, floor1, floor2, floor3, floor4 = tile_read()
    ##  Z0  ##
    if position[2] == 0:
        floor = floor0
        floor = examine_y(position, inventory, statistics, name, character_type, difficulty, floor)
        floor0 = floor
    ##  Z1  ##
    elif position[2] == 1:
        floor = floor1
        floor = examine_y(position, inventory, statistics, name, character_type, difficulty, floor)
        floor1 = floor
    ##  Z2  ##
    elif position[2] == 2:
        floor = floor2
        floor = examine_y(position, inventory, statistics, name, character_type, difficulty, floor)
        floor2 = floor
    ##  Z3  ##
    elif position[2] == 3:
        floor = floor3
        floor = examine_y(position, inventory, statistics, name, character_type, difficulty, floor)
        floor3 = floor
    ##  Z4  ##
    elif position[2] == 4:
        if position[1] == 0:
            if position[0] == 0:
                if floor4[0] == 0:
                    print("You found a health potion!")
                    inventory[0] += 1
                    input("Added to inventory. ^")
                    floor4[0] += 10
                else:
                    input("There's nothing here... ^")
            elif position[0] == 1:
                if floor4[1] == 0:
                    print("You found a health potion!")
                    inventory[0] += 1
                    input("Added to inventory. ^")
                    floor4[1] += 10
                else:
                    input("There's nothing here... ^")
                    secret3.append(0)
            elif position[0] == 2:
                if floor4[2] == 1:
                    print("You found a mana potion!")
                    inventory[1] += 1
                    input("Added to inventory. ^")
                    floor4[2] += 10
                else:
                    input("There's nothing here... ^")
            elif position[0] == 3:
                if floor4[3] == 1:
                    print("You found a mana potion!")
                    inventory[1] += 1
                    input("Added to inventory. ^")
                    floor4[3] += 10
                else:
                    input("There's nothing here... ^")
        elif position[1] == 1:
            if position[0] == 0:
                if floor4[4] == 0:
                    print("You found a health potion!")
                    inventory[0] += 1
                    input("Added to inventory. ^")
                    floor4[4] += 10
                else:
                    input("There's nothing here... ^")
                    secret3.append(7)
            elif position[0] == 1:
                if floor4[5] == 5:
                    boss_battle(inventory, statistics, name, character_type, position, floor4, difficulty)
                else:
                    input("There's nothing here... ^")
                    secret3.append(8)
            elif position[0] == 2:
                if floor4[6] == 5:
                    boss_battle(inventory, statistics, name, character_type, position, floor4, difficulty)
                else:
                    input("There's nothing here... ^")
                    secret3.append(9)
            elif position[0] == 3:
                if floor4[7] == 1:
                    print("You found a mana potion!")
                    inventory[1] += 1
                    input("Added to inventory. ^")
                    floor4[7] += 10
                else:
                    input("There's nothing here... ^")
        elif position[1] == 2:
            if position[0] == 0:
                if floor4[8] == 0:
                    print("You found a health potion!")
                    inventory[0] += 1
                    input("Added to inventory. ^")
                    floor4[8] += 10
                else:
                    input("There's nothing here... ^")
                    secret3.append(4)
            elif position[0] == 1:
                if floor4[9] == 5:
                    boss_battle(inventory, statistics, name, character_type, position, floor4, difficulty)
                else:
                    input("There's nothing here... ^")
                    secret3.append(5)
            elif position[0] == 2:
                if floor4[10] == 5:
                    boss_battle(inventory, statistics, name, character_type, position, floor4, difficulty)
                else:
                    input("There's nothing here... ^")
                    secret3.append(6)
            elif position[0] == 3:
                if floor4[11] == 1:
                    print("You found a mana potion!")
                    inventory[1] += 1
                    input("Added to inventory. ^")
                    floor4[11] += 10
                else:
                    input("There's nothing here... ^")
        elif position[1] == 3:
            if position[0] == 0:
                if floor4[12] == 0:
                    print("You found a health potion!")
                    inventory[0] += 1
                    input("Added to inventory. ^")
                    floor4[12] += 10
                else:
                    input("There's nothing here... ^")
                    secret3.append(1)
            elif position[0] == 1:
                if floor4[13] == 0:
                    print("You found a health potion!")
                    inventory[0] += 1
                    input("Added to inventory. ^")
                    floor4[13] += 10
                else:
                    input("There's nothing here... ^")
                    secret3.append(2)
            elif position[0] == 2:
                if floor4[14] == 1:
                    print("You found a mana potion!")
                    inventory[1] += 1
                    input("Added to inventory. ^")
                    floor4[14] += 10
                else:
                    input("There's nothing here... ^")
                    secret3.append(3)
            elif position[0] == 3:
                if floor4[15] == 1:
                    print("You found a mana potion!")
                    inventory[1] += 1
                    input("Added to inventory. ^")
                    floor4[15] += 10
                else:
                    input("There's nothing here... ^")

    tile_write(floor0, floor1, floor2, floor3, floor4)


def examine_y(position, inventory, statistics, name, character_type, difficulty, floor):
    why = position[1]
    floor = examine_x(position, inventory, statistics, name, character_type, difficulty, floor, why)
    return floor


def examine_x(position, inventory, statistics, name, character_type, difficulty, floor, why):
    add = True
    ex = position[0]
    if why > 0:
        ex += 4 * why
    if floor[ex] == 0:
        print("You found a health potion!")
        inventory[0] += 1
        input("Added to inventory. ^")
    elif floor[ex] == 1:
        print("You found a mana potion!")
        inventory[1] += 1
        input("Added to inventory. ^")
    elif floor[ex] == 2:
        print("There's an enemy!")
        battle(inventory, statistics, name, character_type, position, difficulty)
    elif floor[ex] == 3:
        print("You found a key!")
        inventory[2] += 1
        input("There must be somewhere to use this... ^")
    elif floor[ex] == 4:
        print("You ran into some stairs.")
        if inventory[2] >= 1:
            stair_selection = input("Do you want to go up? ")
            if stair_selection.lower() == "y" or stair_selection == "yes":
                input("You went up the stairs... ^")
                position[2] += 1
                inventory[2] -= 1
                input("As you reached the top, you noticed that the stairs were no longer there... ^")
            else:
                input("'There's some stuff I can still do...' ^")
        else:
            input("But it seems like a key is required to go up them... ^")
    else:
        input("There's nothing here... ^")
    if floor[ex] == 4:
        add = False
    elif floor[ex] == 2:
        add = False
    else:
        add = True
    if add:
        floor[ex] += 10
    return floor


# Allows the player to fight enemies #
def battle(inventory, statistics, name, character_type, position, difficulty):
    mon_type, mon_health, mon_attack, exp_drop = enemy(position, difficulty)
    attack1, attack2, damage1, damage2, mana_reduction = character_attacks(character_type, statistics)
    fighting = True
    while fighting:
        mon_damage = mon_attack
        print(name + " the " + character_type + "'s stats:")
        print("Health: " + str(statistics[0]))
        print("Mana: " + str(statistics[1]) + "\n")
        print(mon_type + "'s stats:")
        print("Health: " + str(mon_health))
        print("\n")
        print("What would you like to do?")
        print("1. Fight")
        print("2. Protect")
        print("3. Take Potion")
        print("4. Run")
        player_turn = input()
        if player_turn == "1":
            print("Which attack would you like to use?")
            print("1. " + attack1)
            print("2. " + attack2 + " (-" + str(mana_reduction) + " mana)")
            which_attack = input()
            if which_attack == "1":
                damage = damage1
                attack = attack1
            elif which_attack == "2":
                damage = damage2
                attack = attack2
                statistics[1] -= mana_reduction
            else:
                damage = damage1
                attack = attack1
            if random.randint(0, 100) > 80:
                input("You suddenly felt a gust of strength flush over you, how strange... ^")
                damage += damage * 0.1
            elif random.randint(0, 100) < 20:
                input("You tripped on nothing while attacking, how strange... ^")
                damage -= damage * 0.1
            input("You used " + attack + " ^")
            mon_health -= damage
            input("You did " + str(damage) + " damage. ^")
        elif player_turn == "2":
            input("You readied yourself for an attack. ^")
            mon_damage /= 2
            input("Incoming damage is halved")
        elif player_turn == "3":
            print("What Kind? ")
            print("1. Health")
            print("2. Mana")
            potion_selection = input()
            if potion_selection == "1":
                if inventory[0] > 0:
                    input("You took a health potion. ^")
                    statistics[0] += 50
                    inventory[0] -= 1
                else:
                    input("You don't have any health potion. ^")
            elif potion_selection == "2":
                if inventory[1] > 0:
                    input("You took a mana potion. ^")
                    statistics[1] += 5
                    inventory[1] -= 1
                else:
                    input("You don't have any mana potions. ^")
        elif player_turn == "4":
            if random.randint(0, 1) == 0:
                input("You ran away successfully. ^")
                break
            else:
                input("You failed to run away. ^")
        if mon_health <= 0:
            fighting = False
            input("You defeated the " + mon_type + "! ^")
            statistics[4] += exp_drop
            input("You gained " + str(exp_drop) + " EXP. ^")
            drop = random.randint(0, 1)
            if drop == 0:
                input("You gained a Health potion! ^")
                inventory[0] += 1
            else:
                input("You gained a Mana potion! ^")
                inventory[1] += 1
            print("\n" * 20)
            break
        print("The " + mon_type + " attacked!")
        statistics[0] -= mon_damage
        input("The " + mon_type + " did " + str(mon_damage) + " damage! ^")
        if statistics[0] <= 0:
            fighting = False
            death(statistics, position, character_type, difficulty)


# If you die, this happens. Stats return to normal#
def death(statistics, position, character_type, difficulty):
    input("Oh my, it seems you've died! ^")
    input("But do not worry, I shall bring you back to life! ^")
    print("\n" * 20)
    print("You've retreated to X: 0 Y: 0")
    input("And you're went back to default. ^")
    position[0] = 0
    position[1] = 0
    if character_type == "knight":
        statistics[0] = 50
        statistics[0] += int(0.25 * (difficulty * statistics[0]))
    elif character_type == "witch":
        statistics[0] = 50
        statistics[0] += int(0.25 * (difficulty * statistics[0]))
    elif character_type == "troll":
        statistics[0] = 50
        statistics[0] += int(0.25 * (difficulty * statistics[0]))
    elif character_type == "healer":
        statistics[0] = 100
        statistics[0] += int(0.25 * (difficulty * statistics[0]))
    elif character_type == "daemon":
        statistics[0] = 100
        statistics[0] += int(0.25 * (difficulty * statistics[0]))
    elif character_type == "villager":
        statistics[0] = 20
        statistics[0] += int(0.25 * (difficulty * statistics[0]))
    elif character_type == "satyr":
        statistics[0] = 50
        statistics[0] += int(0.25 * (difficulty * statistics[0]))
    print("\n" * 20)


# Levels up when EXP reaches different milestones#
def level_up(statistics):
    statistics[4] -= 100
    input("You are leveling up! ^")
    print("\n" * 20)
    statistics[3] += 1
    input("You have leveled up to LVL " + str(statistics[3]) + "! ^")
    statistics[2] += int(statistics[2] * 0.1)
    input("Your power has increased 10% to " + str(statistics[2]) + " ^")


# Looks at X and Y positions to locate the player #
def location(position):
    print("\n" * 20)
    print("Floor: " + str(position[2]))
    print("–––––––––––––––––")
    if position[1] == 0:
        print("|   |   |   |   |")
        print("–––––––––––––––––")
        print("|   |   |   |   |")
        print("–––––––––––––––––")
        print("|   |   |   |   |")
        print("–––––––––––––––––")
        if position[0] == 0:
            print("| X |   |   |   |")
        elif position[0] == 1:
            print("|   | X |   |   |")
        elif position[0] == 2:
            print("|   |   | X |   |")
        elif position[0] == 3:
            print("|   |   |   | X |")
    elif position[1] == 1:
        print("|   |   |   |   |")
        print("–––––––––––––––––")
        print("|   |   |   |   |")
        print("–––––––––––––––––")
        if position[0] == 0:
            print("| X |   |   |   |")
        elif position[0] == 1:
            print("|   | X |   |   |")
        elif position[0] == 2:
            print("|   |   | X |   |")
        elif position[0] == 3:
            print("|   |   |   | X |")
        print("–––––––––––––––––")
        print("|   |   |   |   |")
    elif position[1] == 2:
        print("|   |   |   |   |")
        print("–––––––––––––––––")
        if position[0] == 0:
            print("| X |   |   |   |")
        elif position[0] == 1:
            print("|   | X |   |   |")
        elif position[0] == 2:
            print("|   |   | X |   |")
        elif position[0] == 3:
            print("|   |   |   | X |")
        print("–––––––––––––––––")
        print("|   |   |   |   |")
        print("–––––––––––––––––")
        print("|   |   |   |   |")
    elif position[1] == 3:
        if position[0] == 0:
            print("| X |   |   |   |")
        elif position[0] == 1:
            print("|   | X |   |   |")
        elif position[0] == 2:
            print("|   |   | X |   |")
        elif position[0] == 3:
            print("|   |   |   | X |")
        print("–––––––––––––––––")
        print("|   |   |   |   |")
        print("–––––––––––––––––")
        print("|   |   |   |   |")
        print("–––––––––––––––––")
        print("|   |   |   |   |")
    print("–––––––––––––––––")
    input("^")
    print("\n" * 20)


# The final boss, slightly different to normal battle #
def boss_battle(inventory, statistics, name, character_type, position, floor4, difficulty):
    print("You Encountered The Great Dragon!")
    attack1, attack2, damage1, damage2, mana_reduction = character_attacks(character_type, statistics)
    mon_type = "The Great Dragon"
    mon_health = 1000
    mon_attack = 80
    exp_drop = 2000
    fighting = True
    while fighting:
        mon_damage = mon_attack
        print(name + " the " + character_type + "'s stats:")
        print("Health: " + str(statistics[0]))
        print("Mana: " + str(statistics[1]) + "\n")
        print(mon_type + "'s stats:")
        print("Health: " + str(mon_health))
        print("\n")
        print("What would you like to do?")
        print("1. Fight")
        print("2. Protect")
        print("3. Take Potion")
        print("4. Run")
        player_turn = input()
        if player_turn == "1":
            print("Which attack would you like to use?")
            print("1. " + attack1)
            print("2. " + attack2 + " (-" + str(mana_reduction) + " mana)")
            which_attack = input()
            if which_attack == "1":
                damage = damage1
                attack = attack1
            elif which_attack == "2":
                damage = damage2
                attack = attack2
                statistics[1] -= mana_reduction
            else:
                damage = damage1
                attack = attack1
            if random.randint(0, 100) > 80:
                input("You suddenly felt a gust of strength flush over you, how strange... ^")
                damage += damage * 0.1
            elif random.randint(0, 100) < 20:
                input("You tripped on nothing while attacking, how strange... ^")
                damage -= damage * 0.1
            input("You used " + attack + " ^")
            mon_health -= damage
            input("You did " + str(damage) + " damage. ^")
        elif player_turn == "2":
            input("You readied yourself for an attack. ^")
            mon_damage /= 2
            input("Incoming damage is halved")
        elif player_turn == "3":
            print("What Kind? ")
            print("1. Health")
            print("2. Mana")
            potion_selection = input()
            if potion_selection == "1":
                if inventory[0] > 0:
                    input("You took a health potion. ^")
                    statistics[0] += 50
                    inventory[0] -= 1
                else:
                    input("You don't have any health potion. ^")
            elif potion_selection == "2":
                if inventory[1] > 0:
                    input("You took a mana potion. ^")
                    statistics[1] += 5
                    inventory[1] -= 1
                else:
                    input("You don't have any mana potions. ^")
        elif player_turn == "4":
            if random.randint(0, 1) == 0:
                input("You ran away successfully. ^")
                break
            else:
                input("You failed to run away. ^")
        if mon_health <= 0:
            fighting = False
            input("You defeated " + mon_type + "! ^")
            statistics[4] += exp_drop
            input("You gained " + str(exp_drop) + " EXP. ^")
            drop = random.randint(0, 1)
            if drop == 0:
                input("You gained a Health potion! ^")
                inventory[0] += 1
            else:
                input("You gained a Mana potion! ^")
                inventory[1] += 1
            print("\n" * 20)
            break
        print(mon_type + " attacked!")
        statistics[0] -= mon_damage
        input(mon_type + " did " + str(mon_damage) + " damage! ^")
        if statistics[0] <= 0:
            fighting = False
            death(statistics, position, character_type, difficulty)


# Disables the 4th floor boss #
def innocent_floor4(floor4):
    floor4[5] += 10
    floor4[6] += 10
    floor4[9] += 10
    floor4[10] += 10


# Freddy Fazbear! #
def freddy_fazbear(inventory, statistics, name, character_type, position, difficulty):
    print("You Encountered Freddy Fazbear!")
    attack1, attack2, damage1, damage2, mana_reduction = character_attacks(character_type, statistics)
    mon_type = "Freddy Fazbear"
    mon_health = 10000
    mon_attack = 100
    exp_drop = 2000
    fighting = True
    while fighting:
        mon_damage = mon_attack
        print(name + " the " + character_type + "'s stats:")
        print("Health: " + str(statistics[0]))
        print("Mana: " + str(statistics[1]) + "\n")
        print(mon_type + "'s stats:")
        print("Health: " + str(mon_health))
        print("\n")
        print("What would you like to do?")
        print("1. Fight")
        print("2. Protect")
        print("3. Take Potion")
        print("4. Run")
        player_turn = input()
        if player_turn == "1":
            print("Which attack would you like to use?")
            print("1. " + attack1)
            print("2. " + attack2 + " (-" + str(mana_reduction) + " mana)")
            which_attack = input()
            if which_attack == "1":
                damage = damage1
                attack = attack1
            elif which_attack == "2":
                damage = damage2
                attack = attack2
                statistics[1] -= mana_reduction
            else:
                damage = damage1
                attack = attack1
            if random.randint(0, 100) > 80:
                input("You suddenly felt a gust of strength flush over you, how strange... ^")
                damage += damage * 0.1
            elif random.randint(0, 100) < 20:
                input("You tripped on nothing while attacking, how strange... ^")
                damage -= damage * 0.1
            input("You used " + attack + " ^")
            mon_health -= damage
            input("You did " + str(damage) + " damage. ^")
        elif player_turn == "2":
            input("You readied yourself for an attack. ^")
            mon_damage /= 2
            input("Incoming damage is halved")
        elif player_turn == "3":
            print("What Kind? ")
            print("1. Health")
            print("2. Mana")
            potion_selection = input()
            if potion_selection == "1":
                if inventory[0] > 0:
                    input("You took a health potion. ^")
                    statistics[0] += 50
                    inventory[0] -= 1
                else:
                    input("You don't have any health potion. ^")
            elif potion_selection == "2":
                if inventory[1] > 0:
                    input("You took a mana potion. ^")
                    statistics[1] += 5
                    inventory[1] -= 1
                else:
                    input("You don't have any mana potions. ^")
        elif player_turn == "4":
            if random.randint(0, 1) == 0:
                input("You ran away successfully. ^")
                break
            else:
                input("You failed to run away. ^")
        if mon_health <= 0:
            fighting = False
            input("You defeated " + mon_type + "! ^")
            statistics[4] += exp_drop
            input("You gained " + str(exp_drop) + " EXP. ^")
            drop = random.randint(0, 1)
            if drop == 0:
                input("You gained a Health potion! ^")
                inventory[0] += 1
            else:
                input("You gained a Mana potion! ^")
                inventory[1] += 1
            print("\n" * 20)
            break
        print(mon_type + " attacked!")
        statistics[0] -= mon_damage
        input(mon_type + " did " + str(mon_damage) + " damage! ^")
        if statistics[0] <= 0:
            fighting = False
            death(statistics, position, character_type, difficulty)


# Decides the enemy of a battle #
def enemy(position, difficulty):
    mon_type = "Null"
    mon_health = 10000
    mon_attack = 200
    exp_drop = 5000
    if position[2] == 0:
        monster = random.randint(0, 101)
        if 0 <= monster <= 40:
            mon_type = "Slime"
            mon_health = 50 + (position[2] * 20)
            mon_attack = 10 + (position[2] * 10)
            exp_drop = 10 + (position[2] * 10)
        elif 40 < monster <= 70:
            mon_type = "Lizardonit"
            mon_health = 75 + (position[2] * 20)
            mon_attack = 15 + (position[2] * 10)
            exp_drop = 15 + (position[2] * 10)
        elif 70 < monster <= 90:
            mon_type = "Goblin"
            mon_health = 100 + (position[2] * 20)
            mon_attack = 20 + (position[2] * 10)
            exp_drop = 25 + (position[2] * 10)
        elif 90 < monster <= 99:
            mon_type = "Beastman"
            mon_health = 150 + (position[2] * 20)
            mon_attack = 45 + (position[2] * 10)
            exp_drop = 45 + (position[2] * 10)
        elif monster == 100:
            mon_type = "Dragonit"
            mon_health = 200 + (position[2] * 20)
            mon_attack = 70 + (position[2] * 10)
            exp_drop = 100 + (position[2] * 10)
    elif position[2] == 1:
        monster = random.randint(0, 101)
        if 0 <= monster <= 40:
            mon_type = "Ice Slime"
            mon_health = 50 + (position[2] * 20)
            mon_attack = 10 + (position[2] * 10)
            exp_drop = 10 + (position[2] * 10)
        elif 40 < monster <= 70:
            mon_type = "Ice Lizardonit"
            mon_health = 75 + (position[2] * 20)
            mon_attack = 15 + (position[2] * 10)
            exp_drop = 15 + (position[2] * 10)
        elif 70 < monster <= 90:
            mon_type = "Winter-Plated Goblin"
            mon_health = 100 + (position[2] * 20)
            mon_attack = 20 + (position[2] * 10)
            exp_drop = 25 + (position[2] * 10)
        elif 90 < monster <= 99:
            mon_type = "Coated Beastman"
            mon_health = 150 + (position[2] * 20)
            mon_attack = 45 + (position[2] * 10)
            exp_drop = 45 + (position[2] * 10)
        elif monster == 100:
            mon_type = "Frozen Dragonit"
            mon_health = 200 + (position[2] * 20)
            mon_attack = 70 + (position[2] * 10)
            exp_drop = 100 + (position[2] * 10)
    elif position[2] == 2:
        monster = random.randint(0, 101)
        if 0 <= monster <= 40:
            mon_type = "Fire Slime"
            mon_health = 50 + (position[2] * 20)
            mon_attack = 10 + (position[2] * 10)
            exp_drop = 10 + (position[2] * 10)
        elif 40 < monster <= 70:
            mon_type = "Fire Lizardonit"
            mon_health = 75 + (position[2] * 20)
            mon_attack = 15 + (position[2] * 10)
            exp_drop = 15 + (position[2] * 10)
        elif 70 < monster <= 90:
            mon_type = "Fire-Resistant Goblin"
            mon_health = 100 + (position[2] * 20)
            mon_attack = 20 + (position[2] * 10)
            exp_drop = 25 + (position[2] * 10)
        elif 90 < monster <= 99:
            mon_type = "Ignited Beastman"
            mon_health = 150 + (position[2] * 20)
            mon_attack = 45 + (position[2] * 10)
            exp_drop = 45 + (position[2] * 10)
        elif monster == 100:
            mon_type = "Fire Dragonit"
            mon_health = 200 + (position[2] * 20)
            mon_attack = 70 + (position[2] * 10)
            exp_drop = 100 + (position[2] * 10)
    elif position[2] == 3:
        monster = random.randint(0, 101)
        if 0 <= monster <= 40:
            mon_type = "Big Slime"
            mon_health = 50 + (position[2] * 20)
            mon_attack = 10 + (position[2] * 10)
            exp_drop = 10 + (position[2] * 10)
        elif 40 < monster <= 70:
            mon_type = "Reinforced Lizardonit"
            mon_health = 75 + (position[2] * 20)
            mon_attack = 15 + (position[2] * 10)
            exp_drop = 15 + (position[2] * 10)
        elif 70 < monster <= 90:
            mon_type = "Hobgoblin"
            mon_health = 100 + (position[2] * 20)
            mon_attack = 20 + (position[2] * 10)
            exp_drop = 25 + (position[2] * 10)
        elif 90 < monster <= 99:
            mon_type = "Armored Beastman"
            mon_health = 150 + (position[2] * 20)
            mon_attack = 45 + (position[2] * 10)
            exp_drop = 45 + (position[2] * 10)
        elif monster == 100:
            mon_type = "Dragonspawn"
            mon_health = 200 + (position[2] * 20)
            mon_attack = 70 + (position[2] * 10)
            exp_drop = 100 + (position[2] * 10)
    mon_health += 0.2 * (difficulty * mon_health)
    mon_attack += 0.2 * (difficulty * mon_attack)
    exp_drop += int(0.2 * (difficulty * exp_drop))
    return mon_type, mon_health, mon_attack, exp_drop


# Sets up moves
def character_attacks(character_type, statistics):
    if character_type == "knight":
        attack1 = "Sword Slash"
        damage1 = statistics[2]
        attack2 = "Mana Slash"
        damage2 = 20 + statistics[2]
        mana_reduction = 1
    elif character_type == "witch":
        attack1 = "Wand Attack"
        damage1 = statistics[2]
        attack2 = "Fire Ball"
        damage2 = 50 + statistics[2]
        mana_reduction = 3
    elif character_type == "troll":
        attack1 = "Club Smash"
        damage1 = statistics[2]
        attack2 = "Ice Club"
        damage2 = 20 + statistics[2]
        mana_reduction = 1
    elif character_type == "healer":
        attack1 = "Peaceful Tap"
        damage1 = statistics[2]
        attack2 = "Strong Wind"
        damage2 = 10 + statistics[2]
        mana_reduction = 1
    elif character_type == "daemon":
        attack1 = "Merciless Barrage"
        damage1 = statistics[2]
        attack2 = "Hell Fire"
        damage2 = 50 + statistics[2]
        mana_reduction = 5
    elif character_type == "villager":
        attack1 = "Ladle Throw"
        damage1 = statistics[2]
        attack2 = "Mana Ladle"
        damage2 = 5 + statistics[2]
        mana_reduction = 5
    else:
        attack1 = "Punch"
        damage1 = statistics[2]
        attack2 = "Elemental Punch"
        damage2 = 20 + statistics[2]
        mana_reduction = 1
    return attack1, attack2, damage1, damage2, mana_reduction
