import tkinter as tk
from PIL import Image, ImageTk
import winsound

# ------------- Constants ---------------------
SCREEN_WIDTH = 1350
SCREEN_HEIGHT = 750

GRAVITY_FORCE = 9
JUMP_FORCE = 30
SPEED = 7

TIMED_LOOP = 10

# ------------- Variables ---------------------
keyPressed = []

# ------------- Window ------------------------

window = tk.Tk()
window.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))
window.title("Movement")
# window.attributes("-fullscreen", True)

frame = tk.Frame(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
frame.pack()

canvas = tk.Canvas(frame, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.pack()
bg = Image.open("img/L1.png")
image = ImageTk.PhotoImage(bg)
canvas.create_image(680,360, image=image)
player = Image.open("player3.png")
player_size = player.resize((60,90))
char = ImageTk.PhotoImage(player)
show_player =ImageTk.PhotoImage(player_size)
# imgae_id=canvas.create_image(100,570,image=show_player)

r =Image.open("road.png")
road = ImageTk.PhotoImage(r)

# drawimage
def deawImg(row,col):
    canvas.create_image(30*col,40*row+130,image=img1,anchor="nw",tags="cell")
# ------------- Game --------------------------
canvas.create_rectangle(0, 700, 3000, 650, fill="red", outline="red", tags="PLATFORM")

canvas.create_image(100,660, image=road,tags="PLATFORM")


canvas.create_image(500,610, image=road,tags="PLATFORM")


canvas.create_image(900,550, image=road,tags="PLATFORM")

canvas.create_image(600,350, image=road, tags="PLATFORM")

char = canvas.create_image(100,100, image=show_player)


# ------------- Functions ---------------------

# Check if the player can move by projecting the movement with dx and dy
# If checkGround is True, check if the player is on the ground by projecting the movement with the last coordinate
# Instead of getting the platform list with canvas.find_withtag("PLATFORM"), we could have used a global list
# Return True if the player can move (i.e. is not near any wall), False otherwise
def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.coords(char)
    platforms = canvas.find_withtag("PLATFORM")

    if coord[0] + dx < 0 or coord[0] + dx > SCREEN_WIDTH:
        return False

    if checkGround:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0], coord[1] + dy)
    else:
        overlap = canvas.find_overlapping(coord[0]+dx, coord[1]+dy, coord[0]+dx, coord[1])

    for platform in platforms:
        if platform in overlap:
            return False

    return True


# Jump by moving the player up by force pixels
# Only if the player can move up
# The force parameter is always decreasing by 1 until it reaches 0
# The force should be higher than the gravity force to be able to jump
def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(char, 0, -force)
            window.after(TIMED_LOOP, jump, force-1)


# The start_move function is called when a key is pressed
# It adds the key to the keyPressed list if it is not already in it
# If the keyPressed list was empty, it calls the move function
def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()


# The move function is called every TIMED_LOOP milliseconds
# It checks if the player can move in the direction of the keyPressed list
# It also check if the player is on the ground before jumping
def move():
    if not keyPressed == []:
        x = 0
        if "Left" in keyPressed:
            x -= SPEED
        if "Right" in keyPressed:
            x += SPEED
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
        if check_movement(x):
            canvas.move(char, x, 0)
        window.after(TIMED_LOOP, move)

# The gravity function is called every TIMED_LOOP milliseconds
# It checks if the player can move down by GRAVITY_FORCE pixels
# It is always looping, even if the player can't move down
def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(char, 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)


# The stop_move function is called when a key is released
# It removes the key from the keyPressed list
def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)

gravity()

#___img____________
img1=tk.PhotoImage(file="player3.png")
#sound of game________________________________________________________

def songGame():
    winsound.PlaySound("sound/untitled-123636 (1).wav", winsound.SND_ASYNC | winsound.SND_LOOP )

window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)

window.mainloop()