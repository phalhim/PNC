import tkinter as tk
from PIL import Image , ImageTk
import winsound

# ------------- Constants ---------------------
SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 700

GRAVITY_FORCE = 9
JUMP_FORCE = 27
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
#image_________________________________________________
page1 = tk.PhotoImage(file='img/L1.png')

page2 = tk.PhotoImage(file='img/int_page.png')


play_file = Image.open("player3.png")
play_size = play_file.resize((60, 90))
play = ImageTk.PhotoImage(play_size)
player = canvas.create_image(100, 150, image=play)

canvas.create_rectangle(0,800,SCREEN_WIDTH,SCREEN_HEIGHT,fill="black",tags="PLATFORM")


enter = tk.PhotoImage(file='img/enter.png')
infor = tk.PhotoImage(file='img/info.png')
exit = tk.PhotoImage(file='img/exit.png')
back = tk.PhotoImage(file='img/back.png')
# ------------- Game --------------------------






#  start game___________
def start(event):

    canvas.delete('all')
    
    canvas.create_image(0,0 , image=page1 , anchor='nw')

    # enter button
    canvas.create_image(550,300 , image=enter , anchor='nw' , tags='enter')
    canvas.create_text(588,325 , text='START', font=('Comic Sans MS', 30) , anchor='nw' , tags='enter')
    # info button
    canvas.create_image(500,406 , image=infor , anchor='nw' , tags='info')
    canvas.create_text(555,410 , text='Instruction', font=('Comic Sans MS', 30) , anchor='nw' , tags='info')
    # exit button
    canvas.create_image(550,480 , image=exit , anchor='nw' , tags='exit')
    canvas.create_text(598,505 , text='EXIT', font=('Comic Sans MS', 30) , anchor='nw' , tags='exit')
# #  exit game___________

def exitfromgame(event):
    canvas.quit()

#  info___________
def info(event):
    canvas.create_image(0,-60 , image=page2 , anchor='nw')
    # go back
    canvas.create_image(10,10 , image=back , anchor='nw' , tags='back')
    canvas.create_text(70,35 , text='back', font=('Zorque', 30) , anchor='nw' , tags='back')

def level_one(event):
    canvas.delete('all')
    canvas.create_image(0,-50, image=page1 , anchor='nw')
    player = canvas.create_image(100, 150, image=play)
    coord = canvas.coords(player)
        
    
      
#check movenent_______________________________________________
def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("PLATFORM")

    if coord[0] + dx < 0 or coord[0]+play.width() + dx > SCREEN_WIDTH:
        return False

    if checkGround:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+play.width() , coord[1]+play.height() + dy)
    else:
        overlap = canvas.find_overlapping(coord[0]+dx, coord[1]+dy, coord[0]+dx, coord[1]+play.width())

    for platform in platforms:
        if platform in overlap:
            return False
    return True

def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player, 0, -force)
            window.after(TIMED_LOOP, jump, force-1)

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
            if check_movement(x):
                canvas.move(player, x, 0)
            window.after(TIMED_LOOP, move)
        if "Right" in keyPressed:
            x += SPEED
            if check_movement(x):
                canvas.move(player, x, 0)
            window.after(TIMED_LOOP, move)
            
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
        
def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)

def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)

gravity()

#sound of game________________________________________________________

# def songGame():
#     winsound.PlaySound("sound/untitled-123636 (1).wav", winsound.SND_ASYNC | winsound.SND_LOOP )
# songGame()


#call fucnt___________________________________________________
start(event=start)

# _____________________________button Bind__________________________________

canvas.tag_bind('enter', '<Button-1>',level_one)
canvas.tag_bind('info', '<Button-1>',info)
canvas.tag_bind('exit', '<Button-1>',exitfromgame)
canvas.tag_bind('back', '<Button-1>',start)

#Display______________________________________

window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)

window.mainloop()