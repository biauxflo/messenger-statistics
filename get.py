import os
import re
import json


def getname(name):
    # remove whitspaces
    conv = name.replace(" ", "")
    # lowercase
    conv = conv.lower()
    # regex _*
    # conv = "^'" + conv + "_.*'$"
    # return final conv name
    return conv


def getfile(name):

    originpath = os.getcwd()
    path = os.getcwd() + "/messages/inbox/"
    os.chdir(path)
    oslist = os.listdir()
    r = re.compile(getname(name))
    conv = list(filter(r.match, oslist))
    conv = conv.__getitem__(0)
    os.chdir(path + "/" + conv)
    with open("message_1.json") as messages:
        data = json.load(messages)
    os.chdir(originpath)
    return data
