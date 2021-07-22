import decode


def userlist(data):
    userlist = str(data["participants"])
    userlist = userlist.replace("name", "")
    userlist = userlist.replace("[", "")
    userlist = userlist.replace("]", "")
    userlist = userlist.replace("'", "")
    userlist = userlist.replace('""', "")
    userlist = userlist.replace('{:', "")
    userlist = userlist.replace('}', "")
    return decode.string_decode(userlist)


def usertab(data):
    usertab = userlist(data).split(',')
    for i in range(len(usertab)):
        usertab[i] = str(usertab[i]).strip()
    return usertab


def userdico(data):
    userdict = {}
    for participant in data["participants"]:
        userdict[decode.string_decode(participant["name"])] = None
    return userdict
