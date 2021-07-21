import decode


def userlist(data):
    userlist = str(data["participants"])
    userlist = userlist.replace("name", "")
    userlist = userlist.replace("[", "")
    userlist = userlist.replace("]", "")
    userlist = userlist.replace("'", '"')
    userlist = userlist.replace('""', "")
    userlist = userlist.replace('{:', "")
    userlist = userlist.replace('}', "")
    return decode.string_decode(userlist)
