import tkinter as tk
root =tk.Tk()
root.geometry("600x600")
fram =tk.Frame()
fram.master.title("BU")
canvas =tk.Canvas(fram)
x1 =200
x2 = 250
y1 = 225
y2 = 275
for i in range(5):
    canvas.create_oval(x1,y1,x2,y2,fill="#ff0000")
    x1 += 50
    x2 = x1+50
    y1+=50
    y2=y1+50
canvas.pack(expand=True,fill="both")
fram.pack(expand=True, fill="both")
root.mainloop()