#PyDraw Editor#
#Made by @limr77 On Discord, @franol920
#Importing some basic ass libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msgbox
 #Delete this, export everything into one file, and the renderer is gonna be in a class.
import pdehelp

#Variable Initialization
currproj="Untitled"

#Defining some functions, for menu buttons
def show_helpman():
    pdehelp.showhelp()
def show_credits():
    msgbox.showinfo("Credits", "PyDraw GUI image editor made by @limr77 and @franol920 (Discord)")

#Initalizing stuff
window = Tk()
window.title("PyDraw 0.1B - " + currproj)
window.geometry("1280x720")
helpwindow=PanedWindow(window)
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
    canvas.pack(fill=BOTH, expand=True)
pdengine()
#Creating the file menu
menu = Menu(window)
window.config(menu=menu)

file = Menu(menu)
menu.add_cascade(label='File', menu=file) 
file.add_command(label='New')
file.add_separator()
file.add_command(label='Save')
file.add_command(label='Open') # sprawdz  

#Creating the Edit Menu
edit = Menu(menu)
edit.add_cascade(label="Edit",menu=edit)
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