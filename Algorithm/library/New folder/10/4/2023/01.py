
# def won(event):
#     canvas.create_text(250, 350, text="You won!", font=30)
# def win (event):
#     canvas.create_text(250, 500, text="lost", font=45, colorrand="#FFA07A")

# import tkinter as tk
# from random import randrange
# root = tk.Tk()
# root.geometry("600x600")
# frame = tk.Frame()
# frame.master.title("Hello")
# canvas = tk.Canvas(frame)
# x1 =50
# x2 =90
# y1=100
# y2=130

# colorrand = randrange(0, 8)
# for i in range(9):
#     if i == colorrand:
#         canvas.create_oval(x1,250, x2+50, 300, fill="DFFF00", tags="dog")
#     else:
#         canvas.create_oval(x1,y1,x2,y2,fill="#CCCCFF", tags="cat") 
#     x1 +=40
#     x2=x1+40
# canvas.tag_bind("dog","<button-1>",won )
# canvas.tag_bind("cat","<Button-1>",win)

# canvas.pack(expand=True, fill="both")
# frame.pack(expand=True, fill="both")
# root.mainloop()



def myEventTrigger(event):
    canvas.create_text(250,300,text="You won!",font=45)
def youLost(event):
    canvas.create_text(250,500,text="lost",font=45,colorrand= "blue")
import tkinter as tk
from random  import randrange
root = tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("kkk")
canvas = tk.Canvas(frame)
x1 = 50
x2= 90
y1 = 100
y2 = 130
colorrand=randrange(0,9)
for i in range(10):
    if colorrand == i:
        canvas.create_oval(x1,y1,x2,y2,fill="red",tags="PNC")
    
    else:
        canvas.create_oval(x1,y1,x2,y2,fill="blue",tags="lost")
        
    x1 +=40
    x2 = x1 +40
canvas.tag_bind("lost","<Button-1>",youLost)
canvas.tag_bind("PNC","<Button-1>",myEventTrigger)

canvas.pack(expand=True,fill='both')
frame.pack(expand=True,fill='both')
root.mainloop()