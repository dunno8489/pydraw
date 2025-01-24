import turtle as tkgfx

def initpydrend(title,bgcol,screenW,screenH):
    tkgfx.title(titlestring=title)
    tkgfx.screensize(canvwidth=screenW,canvheight=screenH,bg=bgcol)