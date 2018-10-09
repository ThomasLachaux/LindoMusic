# coding: utf-8

from appdirs import user_data_dir
from os import path
from i18n import _
import musics

# Appdata directory
dataDir = user_data_dir(roaming=True).replace("\\", "/")

# Main Dofus file
filename = dataDir + "/Lindo/game/build/script.js"


def prompt_welcome_message():
    """ Prompts the welcome message and the user makes a choice between which kind of song he chooses"""
    choice = 0
    while choice != 1 and choice != 2 and choice != 3:
        print(_("welcome").format(user_data_dir(roaming=True) + "/Lindo/game"))
        choice = int(input(_("choice")))

    return choice


# noinspection PyUnresolvedReferences
def main():
    choice = prompt_welcome_message()

    if not path.exists(filename):
        raise FileNotFoundError(_("file_not_found").format(filename))

    data = ""

    if choice == 1:
        print(_("1.29"))
        data = musics.m129

    elif choice == 2:
        print(_("2.0"))
        data = musics.m200

    else:
        print(_("reset"))

    linetofind = "settings.getFileUri = function(e, t) {"

    # Opening script.js
    with open(filename, 'r', encoding='utf-8') as file:
        print(_("open_file"))
        filedata = file.readlines()

    # In which line it adds the code
    for i, line in enumerate(filedata):
        if line.find(linetofind) != -1:
            print(_("found").format(i))
            begining_index = line.find(linetofind)

            line = line[:begining_index]
            line = "{}{}{}\n".format(line, linetofind, data)

            filedata[i] = line

    # List to string
    filedata = "".join(filedata)

    # Writing in file
    with open(filename, 'w', encoding='utf-8') as file:
        print(_("writing_file"))
        file.write(filedata)

    print(_("songs_edited"))
    input(_("quit"))


if __name__ == "__main__":
    main()
