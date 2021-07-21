import tri
import get

if __name__ == "__main__":
# demander le nom de la conv à analyser
    name = input("Quel est le nom de la conversation à analyser ?")
# recuperer bonne conversation
    conv = get.get(name)