from locale import getdefaultlocale

language = getdefaultlocale()[0][0:2]


def _(id):
    if id == "welcome":

        if language == "fr":
            return "Bienvenue sur Lindo Music, modifiez rapidement les musiques de Dofus.\n\n/!\ Cet outil (fait à " \
                   "l'arrache ^^) est purement indépendant, je ne suis en aucun cas affilé à Ankama Games /!\ \n Si " \
                   "des bugs sur votre client apparaissent ou que vous voulez revenir aux musiques actuelles, " \
                   "supprimez le dossier {} et relancez Lindo\n\n " \
                   "Quelle version voulez vous choisir ?\n" \
                   "1) 1.29\n" \
                   "2) Ancienne 2.0 (modification d'Amakna et des cania)\n" \
                   "3) Restauration par défaut\n"

        return "Welcome to Lindo Music, edit quickly Dofus Touch songs\n\n" \
               "/!\ This tool was made independently, I am not affiliated to Ankama Games /!\\\n" \
               "If bugs appear on Lindo, juste delete the folder {} and restart Lindo\n" \
               "Which version do you wanna choose ?\n" \
               "1) 1.29\n" \
               "2) Old 2.0 (only Amakna and cania)\n" \
               "3) Reset\n"

    elif id == "choice":

        if language == "fr":
            return "Choix ?"
        return "Choice ?"

    elif id == "file_not_found":

        if language == "fr":
            return "Le fichier {} n'existe pas"
        return "The file {} doesn't exist"

    elif id == "1.29":

        if language == "fr":
            return "Musiques 1.29"

        return "1.29 songs"

    elif id == "2.0":

        if language == "fr":
            return "Musiques 2.0"

        return "2.0 Songs"

    elif id == "reset":

        if language == "fr":
            return "Restauration en cours..."

        return "Reset..."

    elif id == "copy":

        if language == "fr":
            return "Copie des musiques..."

        return "Songs copying..."

    elif id == "open_file":

        if language == "fr":
            return "Ouverture du ficher principal de Dofus Touch"
        return "Opening Dofus touch main file"

    elif id == "found":

        if language == "fr":
            return "Occurence trouvée à la ligne {}"
        return "Found on the line {}"

    elif id == "writing_file":

        if language == "fr":
            return "Ecriture dans le fichier principal"
        return "Writing on the main file"

    elif id == "songs_edited":
        if language == "fr":
            return "Musiques modifiées"
        return "Songs edited !"

    elif id == "quit":
        if language == "fr":
            return "Appuyez sur une touche pour quitter..."

        return "Press any key to continue..."

    else:
        print("Warning ! Sentence {} not translated".format(id))
        return id
