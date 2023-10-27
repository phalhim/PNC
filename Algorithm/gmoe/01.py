import tkinter as tk

scree_Width = 1500
scree_Height = 800
gravity_Force = 8
Jump_Force = 20
speed =5
timed_Loop = 10
keyPressed = []

window = tk.Tk()
window.geometry(str(scree_Width)+"x"+str(scree_Height))
window.title("KOKO")
window.attributes("-fullscreen",True)

frame = tk.Frame(window, width=scree_Width, height=scree_Height)
frame.pack()

canvas = tk.Canvas(frame, width=scree_Width,height=scree_Height)
canvas.pack()

player = canvas.create_rectangle(100, 150, 150, 200, fill="red", outline="red")
canvas.create_rectangle(0, 800, scree_Width, scree_Height, fill="black", tags="PLATFORM")
canvas.create_rectangle(200, 600, 500, 650, fill="black", tags="PLATFORM")
canvas.create_rectangle(600, 700, 650, 850, fill="black", tags="PLATFORM")
canvas.create_rectangle(800, 450, 1100, 500, fill="black", tags="PLATFORM")

def check_movement(dx=0,dy= 0, checkGround =False):
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("PLATFORM")

    if coord[0] + dx < 0 or coord[2] + dx > scree_Width:
        return False

    if checkGround:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[2], coord[3] + dy)
    else:
        overlap = canvas.find_overlapping(coord[0]+dx, coord[1]+dy, coord[2]+dx, coord[3])

    for platform in platforms:
        if platform in overlap:
            return False

    return True


def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player, 0, -force)
            window.after(timed_Loop, jump, force-1)


def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()


def move():
    if not keyPressed == []:
        x = 0
        y = 0
        if "Left" in keyPressed:
            x -= speed
        if "Right" in keyPressed:
            x += speed
        if "Up" in keyPressed:
            y -= speed
        if "space" in keyPressed and not check_movement(0, gravity_Force, True):
            jump(Jump_Force)
        if check_movement(x):
            canvas.move(player, x, 0)
            canvas.move(player,0,y)
        window.after(timed_Loop, move)



def gravity():
    if check_movement(0, gravity_Force, True):
        canvas.move(player, 0, gravity_Force)
    window.after(timed_Loop, gravity)


def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)


gravity()


window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)

window.mainloop()