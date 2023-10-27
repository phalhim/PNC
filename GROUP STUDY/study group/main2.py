import tkinter as tk
import random
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("YOYO")
canvas = tk.Canvas(frame)

color = ["blue","yellow","pink","black","white"]
def draw(event):
    canvas.create_rectangle(event.x,event.y,event.x+20,event.y+20,fill=random.choice(color))
root.bind("<Button-1>",draw)

canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()