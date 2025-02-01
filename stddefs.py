import os as sysapi

def clear():
    if sysapi.name=="nt":
        sysapi.system("cls")
    else:
        sysapi.system("clear")