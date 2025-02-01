#PyDraw Configurator - made by limr77

#Import libraries
from tkinter import *
from tkinter.ttk import *

#Variables
currconfig="config not loaded."

#Initialize Tkinter
configwindow = Tk()
configwindow.title("PyDraw Configurator - " + currconfig)
configwindow.geometry("1280x720")

#Create the configTab for categories
configTabUI=Notebook(configwindow,height=100,width=100)
#generalTab
generalTab=Frame(configTabUI)
#Adding the components to the window
configTabUI.add(generalTab,text="General")
configTabUI.pack(expand=True)
#Run it
configwindow.mainloop()