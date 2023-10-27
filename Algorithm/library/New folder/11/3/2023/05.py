import tkinter as tk
root = tk.Tk()
root.geometry("600x600")
frame =tk.Frame()
frame.master.title("Hello PNC")
canvas =tk.Canvas(frame)
x1 = y1 = 100
x2 = y2 =500
colors = ["red", "blue", "green", "yellow", "green"]
for i in range(5):
    canvas.create_oval(x1, x1, x2, x2, fill=colors[i])
    x1 += 43
    x2 -= 43
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()