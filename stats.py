import decode

def counttalk(usertab, data):
    tmp = ""
    for i in range(len(usertab)):
        tmp = tmp + "0 "
    tmp = tmp.split()
    counttalk = [usertab, tmp]
    messages = data["messages"]
    cpt = 0
    for msg in messages:
        for i in range(len(counttalk[0])):
            if decode.string_decode(msg["sender_name"]) == counttalk[0][i]:
                counttalk[1][i] = int(counttalk[1][i])+1
                cpt += 1
    print("Messages envoyés : " + str(cpt) + " messages\n")
    return counttalk

def printtab(tab):
    for i in range(len(tab[0])):
        print(str(tab[0][i]) + " : " + str(tab[1][i]) + " messages")


def countreacts(data):
    reactions = {}
    messages = data["messages"]
    for msg in messages:
        try:
            for react in msg["reactions"]:
                react = decode.string_decode(react["reaction"])
                if react in reactions:
                    reactions[react] += 1
                else:
                    reactions[react] = 1
        except KeyError:
            pass

    print(reactions)