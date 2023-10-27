import tkinter as tk
import random
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("PU")
canvas = tk.Canvas(frame)
canvas.create_rectangle(0,0,600,600,fill="pink")

color =["blue","pink","black","yellow","orange","brown"]
def drow(event):
    canvas.create_oval(event.x-10, event.y-10, event.x+20, event.y+20, fill=random.choice(color), outline='')
canvas.bind("<B1-Motion>",drow)

canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()