import tkinter as tk

SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 864

SPEED = 7

window = tk.Tk()
window.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))
window.title("Movement")
window.attributes("-fullscreen", True)

frame = tk.Frame(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
frame.pack()

canvas = tk.Canvas(frame, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.pack()

player = canvas.create_rectangle(100, 150, 150, 200, fill="red", outline="red")


def move(event):
    if event.keysym == "Left":
        canvas.move(player, -SPEED, 0)
    elif event.keysym == "Right":
        canvas.move(player, SPEED, 0)
    elif event.keysym == "Up":
        canvas.move(player, 0, -SPEED)
    elif event.keysym == "Down":
        canvas.move(player, 0, SPEED)

window.bind("<Key>", move)

window.mainloop()
