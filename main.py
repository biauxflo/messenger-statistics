import tri
import get
import json
import decode


if __name__ == "__main__":
    # demander le nom de la conv à analyser
    name = str(input("Quel est le nom de la conversation à analyser ? "))
    # get json file
    data = get.getfile(name)  # data = json
    print(json.dumps(data))

    test = "Jules Fi\u00c3\u00a9vet"
    print(decode.string_decode(test))
