import tkinter
import pydraw_gui

canvas=""

def initpdengine():
    canvas = tkinter.Canvas(pydraw_gui.window, bg="white", width=800, height=500)

def start_drawing(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y

def draw(event):
    global start_x, start_y
    canvas.create_line(start_x, start_y, event.x, event.y, fill="black", width=2)
    start_x, start_y = event.x, event.y

def clear_canvas():
    canvas.delete("all")

canvas.bind("<Button-1>", start_drawing) 
canvas.bind("<B1-Motion>", draw)
canvas.pack(fill=tkinter.BOTH, expand=True)
