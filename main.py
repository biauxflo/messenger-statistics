import tri
import recup

if __name__ == "__main__":
#demander le nom de la conv à analyser
    nom = input("Quel est le nom de la conversation à analyser ?")
#recuperer bonne conversation
    conv = recup.recup(nom)