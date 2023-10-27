#library windows
import tkinter as tk
root =tk.Tk()
root.geometry("600x200")
frame =tk.Frame()
frame.master.title("HELLO PNC")
canvas =tk.Canvas(frame)
canvas.create_rectangle(10, 20, 50, 100, fill="#0000FF")
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()