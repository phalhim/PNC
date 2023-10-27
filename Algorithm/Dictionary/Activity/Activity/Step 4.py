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
canvas.create_rectangle(600, 100, 650, 250, fill="black", tags="PLATFORM")


def check_movement(dx):
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("PLATFORM")

    if coord[0] + dx < 0 or coord[2] + dx > SCREEN_WIDTH:
        return False

    overlap = canvas.find_overlapping(coord[0]+dx, coord[1], coord[2]+dx, coord[3])
    for platform in platforms:
        if platform in overlap:
            return False

    return True


def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()


def move():
    if not keyPressed == []:
        x = 0
        if "Left" in keyPressed:
            x -= SPEED
        if "Right" in keyPressed:
            x += SPEED
        if check_movement(x):
            canvas.move(player, x, 0)
        window.after(TIMED_LOOP, move)


def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)


window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)

window.mainloop()
