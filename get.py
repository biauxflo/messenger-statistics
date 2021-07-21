import re
import string


def get(name):
    # remove whitspaces
    conv = name.replace(" ", "")
    # lowercase
    conv = conv.lower()
    # regex _*
    conv = conv + "_.*"
    # return final conv name
    return conv
