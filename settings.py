def settings_access():
    file = open("settings.txt", "r")
    difficulty = int(file.readline().strip())
    auto_examine = int(file.readline().strip())
    return difficulty, auto_examine


def save_settings(difficulty, auto_examine):
    file = open("settings.txt", "w")
    file.write("")
    file.close()
    difficulty = str(difficulty) + "\n"
    auto_examine = str(auto_examine) + "\n"
    file = open("settings.txt", "a")
    file.write(difficulty + auto_examine)
    file.close()


def settings_reset():
    file = open("settings.txt", "w")
    file.write("0\n0\n")
    file.close()