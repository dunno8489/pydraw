import os as sysapi
import pydl

def clear():
    if sysapi.name=="nt":
        sysapi.system("cls")
    else:
        sysapi.system("clear")
def wizard_create():
    print("#LOAD A PROJECT#")
    filename=input()