import tkinter as tk
import winsound

root =tk.Tk()
root.geometry("600x600")
frame =tk.Frame()
frame.master.title("YAYA")
canvas =tk.Canvas(frame)

play=canvas.create_rectangle(10,10,300,70,fill="yellow")
play=canvas.create_rectangle(100,500,300,600,fill="black")
play=canvas.create_rectangle(500,100,400,400,fill="red")
player=canvas.create_oval(100,100,200,200,fill="blue")

def move(event):
    if event.keysym=="Right" and canvas.coords(player)[2]<=canvas.coords(play)[2]:
        canvas.move(player,+10,0)
        print(winsound.PlaySound("you are.wav" , winsound.SND_ASYNC))
    if event.keysym=="Left" and canvas.coords(player)[2]<=canvas.coords(play)[2]:
        canvas.move(player,-10,0)
        print(winsound.PlaySound("02.wav" , winsound.SND_ASYNC))
    if event.keysym =="Down" and canvas.coords(player)[2]<=canvas.coords(play)[2]:
        canvas.move(player,0,+10)
        print(winsound.PlaySound("01.wav" , winsound.SND_ASYNC))
    if event.keysym=="Up" and canvas.coords(player)[2]<=canvas.coords(play)[2]:
        canvas.move(player,0,-10) 
        print(winsound.PlaySound("03.wav" , winsound.SND_ASYNC))

root.bind("<Key>",move)

canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()