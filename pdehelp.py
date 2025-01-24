import tkinter as tk
#Init Code - creates the window, sets the title, sets the window size

#PyDraw Editor Connector

def showhelp():
    #Initalizes the window
    helpwindow = tk.Tk()

    def exithelp():
        helpwindow.destroy()
    #Sets the title of 'helpwindow'
    helpwindow.title("PyDraw Editor Help")
    helpwindow.geometry("1280x720")
    menubar=tk.Menu(helpwindow)
    helpwindow.config(menu=menubar)
    file=tk.Menu(menubar)
    menubar.add_cascade(label="File",menu=file)
    file.add_command(label="Exit", command=exithelp)
    helpwindow.mainloop()