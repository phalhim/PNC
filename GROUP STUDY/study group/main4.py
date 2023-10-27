import tkinter as tk
import random
root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root,width=600,height=600)

def create_random_oval():
    oval_width = random.randint(10,100)
    oval_height = oval_width
    oval_x =random.randint(0,600) 
    oval_y = random.randint(0,600)
    oval_color ='#{:06x}'.format(random.randint(0,0xffffff))
    canvas.create_oval(oval_x, oval_y, oval_x+oval_width, oval_y+oval_height,fill=oval_color)
    root.after(50,create_random_oval)

root.after(50,create_random_oval)
canvas.pack(expand=True,fill="both")
root.mainloop()