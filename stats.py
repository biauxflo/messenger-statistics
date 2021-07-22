import decode
import users

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
    messages = data["messages"]
    participants = users.userdico(data)
    for participant in participants:
        reactions = {}
        for msg in messages:
            try:
                for react in msg["reactions"]:
                    sender = decode.string_decode(react["actor"])
                    react = decode.string_decode(react["reaction"])
                    if participant == sender:
                        if react in reactions:
                            reactions[react] += 1
                        else:
                            reactions[react] = 1
                    participants[participant] = reactions
            except KeyError:
                pass

    for participant in participants:
        print("\n" + participant + " : ")
        for react in participants[participant]:
            print(react, end=' ')
        print("")
        for react in participants[participant]:
            print(participants[participant][react], end=' ')
        print("")

def countunset(data):
    messages = data["messages"]
    participants = users.userdico(data)
    for participant in participants:
        participants[participant] = 0
    for msg in messages:
        if msg["is_unsent"]:
            participants[decode.string_decode(msg["sender_name"])] += 1

    for nb_unsent in participants:
        print(nb_unsent + " : " + str(participants[nb_unsent]))
