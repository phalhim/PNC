import tkinter as tk
import random
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("PO")
canvas = tk.Canvas(frame)

x1 = 0
x2 =55
y1= 0
y2 = 55
color = ["red","yellow","black","pink","blue"]
for i in range(10):
    for j in range(10):
        canvas.create_rectangle(x1,y1,x2,y2,fill=random.choice(color))
        x1 += 55 +5
        x2 = x1 +55
    x1 = 0
    x2 = 55
    y1 += 55+5
    y2 = y1 +55

frame.pack(expand=True,fill="both")
canvas.pack(expand=True,fill="both")
root.mainloop()