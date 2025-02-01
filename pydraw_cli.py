import os as sysapi

renderEngine=""
verbose=False
renderSpeed=0
def clear():
    if sysapi.name=="nt":
        sysapi.system("cls")
    else:
        sysapi.system("clear")



print("PyDraw 0.1B (turtle)")
while(True):
    useri=input("pydraw>")
    if useri.lower()=="clear":
        clear()
    if useri.lower()=="exit":
        exit("Exiting PyDraw and Python...")
    if useri.lower()=="config -render":
        usersub=input("renderPipeline>")
        if usersub.lower()=="turtle":
            renderEngine="turtle"
            print("Rendering Engine set to \'" + renderEngine + "\'.")
        elif usersub.lower()=="pdengine":
            renderEngine="pdengine"
            print("Rendering Engine set to \'" + renderEngine + "\'.")
    if useri.lower()=="config -renderspd":
        usersub=input("renderSpeed>")
        renderSpeed=usersub
        print("Rendering Speed set to " + renderSpeed + ".")
    if useri.lower()=="editor":