import random


# Generates the world tiles randomly during tutorial #
def tile_generation():
    tiles = []
    file = open("tiles.txt", "w")
    file.write("")
    file.close()
    file = open("tiles.txt", "a")
    for ii in range(0, 4):
        has_stair = False
        has_key = False
        for i in range(0, 16):
            to_append = random.randint(0, 4)
            if to_append == 3 and has_key:
                to_append = random.randint(0, 2)
            elif to_append == 3 and not has_key:
                has_key = True
            if to_append == 4 and has_stair:
                to_append = random.randint(0, 2)
            elif to_append == 4 and not has_stair:
                has_stair = True
            tiles.append(to_append)
        if has_stair == False:
            tiles[15] = 4
            if has_key == False:
                tiles[14] = 3
        if has_key == False:
            tiles[15] = 3
            if has_stair == False:
                tiles[14] = 4
    for tile in tiles:
        file.write(str(tile) + "\n")
    file.write("0\n0\n1\n1\n0\n5\n5\n1\n0\n5\n5\n1\n0\n0\n1\n1")
    file.close()


# Reads tile file to access tile status in game #
def tile_read():
    file = open("tiles.txt", "r")
    floor0 = []
    floor1 = []
    floor2 = []
    floor3 = []
    floor4 = []
    for tile0 in range(0, 16):
        floor0.append(int(file.readline().strip()))
    for tile1 in range(0, 16):
        floor1.append(int(file.readline().strip()))
    for tile2 in range(0, 16):
        floor2.append(int(file.readline().strip()))
    for tile3 in range(0, 16):
        floor3.append(int(file.readline().strip()))
    for tile4 in range(0, 16):
        floor4.append(int(file.readline().strip()))
    file.close()
    return floor0, floor1, floor2, floor3, floor4


# Saves tile status to tile file #
def tile_write(floor0, floor1, floor2, floor3, floor4):
    file = open("tiles.txt", "w")
    file.write("")
    file.close()
    file = open("tiles.txt", "a")
    for tile in floor0:
        file.write(str(tile) + "\n")
    for tile in floor1:
        file.write(str(tile) + "\n")
    for tile in floor2:
        file.write(str(tile) + "\n")
    for tile in floor3:
        file.write(str(tile) + "\n")
    for tile in floor4:
        file.write(str(tile) + "\n")
    file.close()

# Resets tiles to all 0s
def tile_reset():
    file = open("tiles.txt", "w")
    file.write("")
    file.close()
    file = open("tiles.txt", "a")
    for num in range(80):
        file.write("0\n")