#PyDraw Editor#
#Made by @limr77 On Discord, @franol920
#Importing some basic ass libraries
from os import *
from os import system as sys
from os import chdir
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msgbox
from tkinter import filedialog as filepick
import pdehelp

#Variable Initialization
currproj="Untitled"

#Initalizing stuff
window = Tk()
propwindow = Tk()
window.title("PyDraw 0.1B - " + currproj)
chdir("img")
window.wm_iconbitmap("window_icon16.ico")
window.wm_iconbitmap("window_icon24.ico")
chdir("..")
propwindow.title("PyDraw Configurator")
propwindow.minsize(400,400)
propwindow.maxsize(800,800)
window.geometry("1280x720")
helpwindow=PanedWindow(window)

#Defining some functions, for menu buttons
def show_helpman():
    pdehelp.showhelp()
def show_credits():
    msgbox.showinfo("Credits", "PyDraw GUI image editor made by @limr77 and @franol920 (Discord)")
def load_proj():
    fileexts=(("PyDraw Projects","*.svg"),("All files", "*.*"))
    currproj=filepick.askopenfilename(filetypes=fileexts,title="Open PyDraw Project")
    if currproj.lower() == "":
        window.title("PyDraw 0.1B - " + "Untitled")
    window.title("PyDraw 0.1B - "+currproj)
def saveas_proj():
    fileexts=(("PyDraw Projects","*.svg"),("All files", "*,*"))
    currproj=filepick.asksaveasfilename(title="Save PyDraw Project as",filetypes=fileexts)

#Initalizing Class libraries (pdengine for example)
class pdengine: 
    canvas = Canvas(window, bg="white", width=800, height=500)

    def start_drawing(event):
        global start_x, start_y
        start_x, start_y = event.x, event.y

    def draw(event):
        global start_x, start_y
        pdengine.canvas.create_line(start_x, start_y, event.x, event.y, fill="black", width=2)
        start_x, start_y = event.x, event.y

    def clear_canvas():
        pdengine.canvas.delete("all")
    canvas.bind("<Button-1>", start_drawing) 
    canvas.bind("<B1-Motion>", draw)
    canvas.place(x=0,y=0)
pdengine()
#Creating the file menu
menu = Menu(window)
window.config(menu=menu)

file = Menu(menu)
menu.add_cascade(label='File', menu=file) 
file.add_command(label='New')
file.add_separator()
file.add_command(label='Save')
file.add_command(label="Save As...",command=saveas_proj)
file.add_command(label='Open',command=load_proj) # sprawdz  

#Creating the Edit Menu
edit = Menu(menu)
menu.add_cascade(label="Edit",menu=edit)
edit.add_command(label='Shapes')
edit.add_command(label='Add Predefined Shapes')
edit.add_separator()
edit.add_command(label='Preferences')

#Creating the Help Menu
Help = Menu(menu)
menu.add_cascade(label='Help',menu=Help)
Help.add_command(label="Help", command=show_helpman)
Help.add_command(label='Credits', command=show_credits)


window.mainloop()