import decode
import users

def counttalk(data):
    messages = data["messages"]
    participants = users.userdico(data)
    for participant in participants:
        participants[participant] = 0
    for msg in messages:
        if not msg["is_unsent"]:
            participants[decode.string_decode(msg["sender_name"])] += 1

    for nb_talk in participants:
        print(nb_talk + " : " + str(participants[nb_talk]))


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
