import tri
import get
import users
import json
import decode


if __name__ == "__main__":
    # demander le nom de la conv à analyser
    name = str(input("Quel est le nom de la conversation à analyser ? "))
    # get json file
    data = get.getfile(name)  # data = json
    # choose action to do
    choice = 0
    while choice != 3:
        choice = int(input("\n1 - Afficher les messages\n2 - Afficher les participants\n3 - Quitter l\'application\n"))
        if choice == 1:
            print(data)
        if choice == 2:
            print(users.userlist(data))
