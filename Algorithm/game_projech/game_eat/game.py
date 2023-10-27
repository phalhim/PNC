import tkinter as tk
from tkinter import *
from PIL import Image , ImageTk
import winsound
import random
from random import randrange


# ---------------------------------------------------------------------------
#=> CONSTANT
# ---------------------------------------------------------------------------
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 740
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
root.title('Super runner')
canvas = tk.Canvas(root)

#-------------------
GRAVITY_FORCE = 9
JUMP_FORCE = 30
SPEED = 7

TIMED_LOOP = 10
#-------------------


# ---------------------------------------------------------------------------

# _________________________________________Images______________________________

icon = tk.PhotoImage(file='image/hero.png')
root.iconphoto(True,icon)
root.resizable(0,0)

game_play = tk.PhotoImage(file="image/background.png")
game_start = tk.PhotoImage(file="image/game_start.png")
game_win = tk.PhotoImage(file="image/game_win.png")
game_help = tk.PhotoImage(file="image/game_help.png")
game_over = tk.PhotoImage(file="image/game_over.png")

hero = tk.PhotoImage(file="image/hero.png")

small_Virus = tk.PhotoImage(file="image/virus_small.png")
big_Virus = tk.PhotoImage(file="image/virus_big.png")
died_Virus = tk.PhotoImage(file="image/virus_died.png")
bulletKill = tk.PhotoImage(file="image/bullet.png")

cash_img = tk.PhotoImage(file="image/cash.png")
heard = tk.PhotoImage(file="image/heard.png")
heard_black = tk.PhotoImage(file="image/heard_black.png")

btn_start_game = tk.PhotoImage(file="image/btn_start_game.png")
btn_exit_game = tk.PhotoImage(file="image/btn_exit_game.png")
btn_help_game = tk.PhotoImage(file="image/btn_help_game.png")
btn_back = tk.PhotoImage(file="image/btn_back.png")
btn_replay = tk.PhotoImage(file="image/btn_replay.png")
btn_retry = tk.PhotoImage(file="image/btn_retry.png")

boom_file = Image.open("image/bom.png")
boom_size = boom_file.resize((60, 60))
boom_img = ImageTk.PhotoImage(boom_size)

#friuts____________________________
apple_img = tk.PhotoImage(file='image/apple.png')
bery_img = tk.PhotoImage(file='image/bery.png')
chery_img = tk.PhotoImage(file='image/chery.png')
mango_img = tk.PhotoImage(file='image/mango.png')

fruits = [apple_img, bery_img, chery_img, mango_img]
#___________________________
way_player =tk.PhotoImage(file='road.png')

#-------Variable----------------------------------

player_X = 150
player_Y = 650
enamy_x = 1400
listOfLives = []
listOfCash = []
listOfBom = []
canLive = 6
toConfig = 0
totalCash = 0
totalBom = 0
isStart = True
#---
count_create_cash = 0
count_create_bom = 0
#--------
keyPressed = []

# ---------------------------------------------------------------------------

#-----------------------FUNCTIONS GAME-------------------------------------
# ==============> Game Process <==================
def processGame():
    if totalCash > 100:
        gameWin()
    if totalBom > 6:
        gameOver()
    canvas.after(100, processGame)

# ==================> Game Show <=================
def gameShow(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_start)
    canvas.create_image(680,280, image=btn_start_game, tags="startgame")
    canvas.create_image(680,410,image=btn_exit_game, tags="exit")
    canvas.create_image(680,540,image=btn_help_game, tags="help")

# ===============> Game Start <===================
def gameStart(event):
    global player, displayTotalBom, displayNumeberBullet, displayTotalCash
    canvas.delete("all")
    canvas.create_image(680, 372,  image=game_play)
    player = canvas.create_image(player_X, player_Y, image=hero)
    canvas.create_image(150, 780, image=way_player,tags="PLATFORM")
    canvas.create_image(700, 780, image=way_player,tags="PLATFORM")
    displayTotalBom = canvas.create_text(1087, 47, text=totalBom, font=("serif", 18 ,'bold'), fill="black")
    displayTotalCash = canvas.create_text(1200, 47, text=totalCash, font=("serif", 18 ,'bold'), fill="black")
    # displayNumeberBullet = canvas.create_text(1310, 47, text=numberOfBullet, font=("serif", 18 ,'bold'), fill="black")
    
    for i in range(6):
        lives = canvas.create_image(65 + i * 37, 45, image=heard)
        listOfLives.append(lives)
    
    create_cash()
    create_bom()
    gravity()
    winsound.PlaySound("sound/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

# =================> Game Win <===================
def gameWin():
    global isStart
    isStart = False
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_win)
    canvas.create_text(1200, 143, text=totalCash, font=("serif", 34 ,'bold'), fill="black")
    # canvas.create_text(1200, 218, text=numberOfBullet, font=("serif", 34 ,'bold'), fill="black")
    canvas.create_image(680,420, image=btn_replay, tags="replay")
    canvas.create_image(680,550,image=btn_exit_game, tags="exit")

# =================> Game Over <==================
def gameOver():
    global isStart
    isStart = False
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_over)
    # canvas.create_text(1200, 143, text=killVirus, font=("serif", 34 ,'bold'), fill="black")
    canvas.create_text(1200, 218, text=totalCash, font=("serif", 34 ,'bold'), fill="black")
    # canvas.create_text(1200, 293, text=numberOfBullet, font=("serif", 34 ,'bold'), fill="black")
    canvas.create_image(680,440, image=btn_retry, tags="replay")
    canvas.create_image(680,570,image=btn_exit_game, tags="exit")

# ==================> Game Help <==================
def game_help(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_help)
    canvas.create_image(140, 200, image=btn_back, tags="back")

# ==================> Game Exit <==================
def gameExit(event):
    root.destroy()

# ================> Game Restart <=================
def game_restart(event):
    global player_X,player_Y,canLive,toConfig,totalCash,totalBom,isStart,listOfLives,listOfCash,listOfBom
    isStart = True
    player_X = 150
    player_Y = 650
    canLive = 6
    toConfig = 0
    totalCash = 0
    totalBom = 0
    listOfLives = []
    listOfCash = []
    listOfBom = []
    gameStart(event)
#-----------------------------Move Player------------------------------
#___________Player Right_____________
def move_right(event):
  global player_X
  if player_X < SCREEN_WIDTH:
    player_X += 30
    canvas.moveto(player, player_X)

#___________Player Left_____________
def move_left(event):
  global player_X
  if player_X > 0:
    player_X -= 30
    canvas.moveto(player, player_X)

#____________________Player Jump______________

def check_movement(dx=0, dy=0, checkGround=False):
    global player
    coord = canvas.coords(player)
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

def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player, 0, -force)
            root.after(TIMED_LOOP, jump, force-1)

def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()

def move():
    if not keyPressed == []:
        x = 0
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
        if check_movement(x):
            canvas.move(player, x, 0)
        root.after(TIMED_LOOP, move)

def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
    root.after(TIMED_LOOP, gravity)

def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)

#---------------------------------------------------
# ==========> Delete Bullet, Virus, And Cash <============
def delete_item(item):
    canvas.delete(item)


# ====================> Create Cash <====================== 
def create_cash():
    global count_create_cash, enamy_x 
    count_create_cash += 1
    enamy_y = randrange(360,655)
    speed_create = randrange(2500,8000)
    cash =canvas.create_image(enamy_x,enamy_y, image=fruits[random.randrange(0,4)] )
    move_cash(cash)
    if isStart and count_create_cash < 50:
        canvas.after(speed_create, lambda:create_cash())
# ====================> Move Cash <========================
def move_cash(cash):
    global totalCash
    canvas.move(cash, -3, 0)
    listOfCash.append(cash)
    positionCash = canvas.coords(cash)
    positionPlayer = canvas.coords(player)
    if len(positionCash) > 0:
        if (positionPlayer[0]+10 >= positionCash[0] and positionPlayer[0]-30 <= positionCash[0]) and (positionPlayer[1] <= positionCash[1]+20 and positionPlayer[1] >=  positionCash[1]-80):
            totalCash += 3
            delete_item(cash)
            canvas.itemconfig(displayTotalCash, text=totalCash)
            winsound.PlaySound("sound/cash.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
        elif positionCash[0] < 0:
            delete_item(cash)
    canvas.after(30, lambda:move_cash(cash))  

# ====================> Create Boom <====================== 
def create_bom():
    global count_create_bom, enamy_x
    count_create_bom += 1
    enamy_y = randrange(500,655)
    speed_create = randrange(4500,9000)
    bom =canvas.create_image(enamy_x,enamy_y, image=boom_img )
    move_bom(bom)
    if isStart and count_create_bom < 50:
        canvas.after(speed_create, lambda:create_bom())

# ====================> Move Boom <========================
def move_bom(bom):
    global totalBom
    canvas.move(bom, -3, 0)
    listOfBom.append(bom)
    positionBom = canvas.coords(bom)
    positionPlayer = canvas.coords(player)
    if len(positionBom) > 0:
        if (positionPlayer[0] +20 >= positionBom[0] and positionPlayer[0]-20 <= positionBom[0]) and (positionPlayer[1]-20 <= positionBom[1]+20 and positionPlayer[1]+40 >=  positionBom[1]-20):
            totalBom += 1
            delete_item(bom)
            canvas.itemconfig(displayTotalBom, text=totalBom)
            winsound.PlaySound("sound/cash.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
        elif positionBom[0] < 0:
            delete_item(bom)
    canvas.after(50, lambda:move_bom(bom))  


# ====================> Draw Can Live <====================
def createCanLive():
    for i in range(canLive):
        live = canvas.create_image(i*37+40, 40, image=heard)
        delete_item(live)

    for i in range(canLive):
        live = canvas.create_image(i*37+40, 40, image=heard)
        delete_item(live)

# ---------------------------------------------------------------------------
#_____________________________CREATE GAME SHOW______________________________
# ---------------------------------------------------------------------------
canvas.create_image(680, 372, image=game_start)
canvas.create_image(680,280, image=btn_start_game, tags="startgame")
canvas.create_image(680,410,image=btn_exit_game, tags="exit")
canvas.create_image(680,540,image=btn_help_game, tags="help")
winsound.PlaySound("sound/open.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
#___________________________AUTO PLAY_____________________________________
processGame()

# ---------------------------------------------------------------------------
#_________________________ALLOW WINDOWS KEYS AND TAGES BIND____________________________
# ---------------------------------------------------------------------------
root.bind("<Right>", move_right)
root.bind("<Left>", move_left)
#---------
root.bind("<Key>", start_move)
root.bind("<KeyRelease>", stop_move)
#---------
canvas.tag_bind("startgame","<Button-1>", gameStart)
canvas.tag_bind("replay","<Button-1>", game_restart)
canvas.tag_bind("back","<Button-1>", gameShow)
canvas.tag_bind("exit","<Button-1>", gameExit)
canvas.tag_bind("help","<Button-1>", game_help)






import tkinter as tk
from PIL import Image, ImageTk

WIN_WIDTH = 1350
WIN_HEIGHT = 750
SCROLLING_SPEED = 5
root = tk.Tk()
root.geometry(str(WIN_WIDTH) + "x" + str(WIN_HEIGHT))
frame = tk.Frame()
canvas = tk.Canvas(frame)
original_image = Image.open("image/background.png")
image_resize = original_image.resize((WIN_WIDTH, WIN_HEIGHT))
background_image = ImageTk.PhotoImage(image_resize)

background_image_label_1= canvas.create_image(0, 0,anchor=tk.NW, image=background_image)
background_image_label_2= canvas.create_image(WIN_WIDTH,0,anchor=tk.NW, image=background_image)


def scroll_bg_image():
    
    canvas.move(background_image_label_1, -1, 0)
    canvas.move(background_image_label_2, -1, 0)

    if canvas.coords(background_image_label_1)[0]< -WIN_WIDTH:
        canvas.coords(background_image_label_1, WIN_WIDTH, 0)
    elif canvas.coords(background_image_label_2)[0]< -WIN_WIDTH:
        canvas.coords(background_image_label_2, WIN_WIDTH, 0)
    canvas.after(5, scroll_bg_image)

scroll_bg_image()





# ---------------------------------------------------------------------------
#__________________________Display ROOT________________________________
# ---------------------------------------------------------------------------
canvas.pack(expand=True, fill='both')
root.mainloop()