import tkinter as tk
import winsound
scree_WIDTH =9000
scree_HEIHT=500
window = tk.Tk()
window.geometry(str(scree_WIDTH)+"x"+str(scree_HEIHT))
frame = tk.Frame()
frame.master.title("KAKA")
frame.pack()
canvas = tk.Canvas(frame)
canvas.pack()
play=canvas.create_rectangle(100,200,200,300,fill="red")
play=canvas.create_rectangle(300,500,500,300,fill="red")
play=canvas.create_rectangle(500,900,900,300,fill="red")

player=canvas.create_oval(100,100,50,50,fill="blue")

canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
window.mainloop()