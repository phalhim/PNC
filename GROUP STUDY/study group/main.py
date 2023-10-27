import tkinter as tk
WIN_WIDTH =600
WIN_HEIGHT =600
root = tk.Tk()
root.geometry(str(WIN_WIDTH)+ "x" +str(WIN_HEIGHT))
frame = tk.Frame()
frame.master.title("Move player")
canvas = tk.Canvas(frame)

player = canvas.create_rectangle(20,20,200,200,fill="red")
def move(event):
    if event.keysym == "Left" and canvas.coords(player)[0]>0:
        canvas.move(player,-10, 0)
    elif event.keysym == "Right" and canvas.coords(player)[2]<WIN_WIDTH:
        canvas.move(player, 10, 0)
    elif event.keysym == "Up" and canvas.coords(player)[1]>0:
        canvas.move(player,0,-10)
    elif event.keysym == "Down" and canvas.coords(player)[3]<WIN_HEIGHT:
        canvas.move(player,0,10)
    print(canvas.coords(player))
root.bind("<Key>", move)

frame.pack(expand=True, fill="both")
canvas.pack(expand=True, fill="both")
root.mainloop()