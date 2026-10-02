from tiles import tile_write, tile_reset
from settings import save_settings, settings_reset

# Allows access to save file information #
def save_access():
    file = open("savegame.txt", "r")
    position = [int(file.readline().strip()), int(file.readline().strip()), int(file.readline().strip())]
    inventory = [int(file.readline().strip()), int(file.readline().strip()), int(file.readline().strip())]
    statistics = [float(file.readline().strip()), int(file.readline().strip()), float(file.readline().strip()), int(file.readline().strip()), float(file.readline().strip())]
    name = file.readline().strip()
    character_type = file.readline().strip()
    tutorial = int(file.readline().strip())
    file.close()
    return position, inventory, statistics, name, character_type, tutorial


# Saves all current information to proper files #
def create_save(position, inventory, statistics, name, character_type, tutorial, floor0, floor1, floor2, floor3, floor4, difficulty, auto_examine):
    file = open("savegame.txt", "w")
    xyz = 0
    thing = 0
    stat = 0
    name = name + "\n"
    character_type = character_type + "\n"
    for number in position:
        if xyz == 0:
            posx = number
            posx = str(posx) + "\n"
        elif xyz == 1:
            posy = number
            posy = str(posy) + "\n"
        elif xyz == 2:
            posz = number
            posz = str(posz) + "\n"
        xyz += 1
    for stuff in inventory:
        if thing == 0:
            health_potions = stuff
            health_potions = str(health_potions) + "\n"
        elif thing == 1:
            mana_potions = stuff
            mana_potions = str(mana_potions) + "\n"
        elif thing == 2:
            keys = stuff
            keys = str(keys) + "\n"
        thing += 1
    for statistic in statistics:
        if stat == 0:
            health = statistic
            health = str(health) + "\n"
        elif stat == 1:
            mana = statistic
            mana = str(mana) + "\n"
        elif stat == 2:
            power = statistic
            power = str(power) + "\n"
        elif stat == 3:
            level = statistic
            level = str(level) + "\n"
        elif stat == 4:
            exp = statistic
            exp = str(exp) + "\n"
        stat += 1
    file.write(posx + posy + posz + health_potions + mana_potions + keys + health + mana + power + level + exp + name + character_type + str(tutorial))
    file.close()
    tile_write(floor0, floor1, floor2, floor3, floor4)
    save_settings(difficulty, auto_examine)


# Starts the game over completely to all defaults. Doesn't include tiles #
def start_over():
    file = open("savegame.txt", "w")
    file.write("0\n0\n0\n0\n0\n0\n0.0\n0\n0\n1\n0\nJuan\nsatyr\n0")
    settings_reset()
    tile_reset()
    file.close()
