import tkinter as tk

SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 864

SPEED = 7
TIMED_LOOP = 10

keyPressed = []

window = tk.Tk()
window.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))
window.title("Movement")
window.attributes("-fullscreen", True)

frame = tk.Frame(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
frame.pack()

canvas = tk.Canvas(frame, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.pack()

player = canvas.create_rectangle(100, 150, 150, 200, fill="red", outline="red")


def check_left_border():
    coord = canvas.coords(player)
    return coord[0] < 0


def check_right_border():
    coord = canvas.coords(player)
    return coord[2] > SCREEN_WIDTH


def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()


def move():
    if not keyPressed == []:
        x = 0
        if "Left" in keyPressed and not check_left_border():
            canvas.move(player, -SPEED, 0)
        if "Right" in keyPressed and not check_right_border():
            canvas.move(player, SPEED, 0)
        window.after(TIMED_LOOP, move)


def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)


window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)

window.mainloop()
