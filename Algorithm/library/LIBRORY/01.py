from tkinter import Tk, Label
from PIL import Image, ImageTk
root =Tk()
img=ImageTk.PhotoImage(file="/img/a1.jpq")
tk_img =ImageTk.PhotoImage(img)
label =Label(root,image=tk_img)
label.pack()
root.mainloop()