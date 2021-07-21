import tri
import get


if __name__ == "__main__":
    # demander le nom de la conv à analyser
    name = str(input("Quel est le nom de la conversation à analyser ?"))
    # give regex of conversation name
    conv = get.getname(name)
    get.getfile(conv)
