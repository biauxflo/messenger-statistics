import decode

def counttalk(usertab, data):
    tmp = ""
    print(len(usertab))
    print("\n")
    for i in range(len(usertab)):
        tmp = tmp + "0 "
    tmp = tmp.split()
    counttalk = [usertab, tmp]
    messages = data["messages"]
    for msg in messages:
        for i in range(len(counttalk[0])):
            if decode.string_decode(msg["sender_name"]) == counttalk[0][i]:
                counttalk[1][i] = int(counttalk[1][i])+1
    return counttalk


def printtab(tab):
    for i in range(len(tab[0])):
        print(str(tab[0][i]) + " : " + str(tab[1][i]) + " messages")
