import decode
import users


def lasttalk(data):
    messages = data["messages"]
    last_msg = users.userdico(data)
    for participant in last_msg:
        for msg in messages:
            if decode.string_decode(msg["sender_name"]) == participant:
                last_msg[participant] = decode.timestamp_decode(msg["timestamp_ms"])
                break

    for participant in last_msg:
        print(participant + " : " + str(last_msg[participant]))



def counttalk(data):
    messages = data["messages"]
    participants = users.userdico(data)
    for participant in participants:
        participants[participant] = 0
    for msg in messages:
        if not msg["is_unsent"]:
            try:
                participants[decode.string_decode(msg["sender_name"])] += 1
            except KeyError:
                participants["Autres"] += 1

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
            try:
                participants[decode.string_decode(msg["sender_name"])] += 1
            except KeyError:
                participants["Autres"] += 1

    for nb_unsent in participants:
        print(nb_unsent + " : " + str(participants[nb_unsent]))


def countwords(data):
    messages = data["messages"]
    count_words = {}
    for msg in messages:
        try:
            message = decode.string_decode(msg["content"])
            message = message.replace("\'", " ")
            message = message.replace("???", " ")
            if ("a rejoint la discussion" not in message) and ("a rejoint l appel" not in message) and ("la discussion vid??o est termin??e"):
                for word in message.split():
                    if len(word) > 5:
                        if word in count_words:
                            count_words[word] += 1
                        else:
                            count_words[word] = 1
        except KeyError:
            pass

    sorted_keys = sorted(count_words, key=count_words.get, reverse=True)

    i = 0;
    for i in range(10):
        print(sorted_keys[i] + " : " + str(count_words[sorted_keys[i]]))


def countspecificword(data):
    messages = data["messages"]
    searched_word = input("Quel mot voulez-vous cherchez dans la conversation ? ")
    count_word = 0;
    for msg in messages:
        try:
            message = decode.string_decode(msg["content"])
            message = message.replace("\'", " ")
            message = message.replace("???", " ")
            for word in message.split():
                if word == searched_word:
                    count_word += 1
        except KeyError:
            pass

    print("Le mot " + searched_word + " apparait " + str(count_word) + " fois.")