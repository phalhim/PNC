import tkinter as tk
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("OG")
crame = tk.Canvas(frame)
x1 = 10
y1 = 50
x2 = 50
y2 = 90
color=[0,8]
for i in range(3):
    crame.create_oval(x1,y1,x2,y2,fill=color)
    