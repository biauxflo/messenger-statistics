import tri
import get
import users
import json
import decode
import stats
import os


if __name__ == "__main__":
    # demander le nom de la conv à analyser
    originpath = os.getcwd()
    name = '.'
    # choose action to do
    choice = 0
    while choice != 8:
        if name == '.':
            choice = 5
        else :
            choice = input("\n1 - Afficher les messages\n2 - Afficher les participants\n3 - Afficher les statistiques\n4 - Afficher les reactions\n5 - Changer de conversation\n6 - Nombre de messages supprimés\n7 - Classement des mots\n8 - Quitter l\'application\n")
            try:
                choice = int(choice)
            except ValueError:
                choice = 0
        if choice == 1:
            print(data)
        if choice == 2:
            print(users.usertab(data))
        if choice == 3:
            stats.counttalk(data)
        if choice == 4:
            stats.countreacts(data)
        if choice == 5:
            name = '.'
            while name == '.':
                name = str(input( "\nQuel est le nom de la conversation à analyser ? \n"))
                # get json file
                try:
                    data = get.getfile( name )  # data = json
                except IndexError:
                    os.chdir( originpath )
                    print( "Désolé, Conversation non trouvée." )
                    name = '.'
        if choice == 6:
            stats.countunset(data)
        if choice == 7:
            stats.countwords(data)