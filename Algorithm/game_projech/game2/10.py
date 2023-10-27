# import tkinter as tk
# from PIL import Image, ImageTk
# import random

# WIN_WIDTH = 1350
# WIN_HEIGHT = 750
# SCROLLING_SPEED = 5
# root = tk.Tk()
# root.geometry(str(WIN_WIDTH) + "x" + str(WIN_HEIGHT))
# frame = tk.Frame()
# canvas = tk.Canvas(frame)
# original_image = Image.open("img/bg.jpg")
# image_resize = original_image.resize((WIN_WIDTH, WIN_HEIGHT))
# background_image = ImageTk.PhotoImage(image_resize)

# background_image_label_1= canvas.create_image(0, 0,anchor=tk.NW, image=background_image)
# background_image_label_2= canvas.create_image(WIN_WIDTH,0,anchor=tk.NW, image=background_image)

# robot_img =Image.open("img/cat.png")
# image_resize1= robot_img.resize((100,100))
# img_robot = ImageTk.PhotoImage(image_resize1)
# character = canvas.create_image(100,600,image=img_robot)

# def move_up(event):
#     canvas.move(character, 0, -10)

# def move_down(event):
#     canvas.move(character, 0, 10)

# def move_left(event):
#     canvas.move(character, -10, 0)

# def move_right(event):
#     canvas.move(character, 10, 0)



# def scroll_bg_image():
    
#     canvas.move(background_image_label_1, -1, 0)
#     canvas.move(background_image_label_2, -1, 0)

#     if canvas.coords(background_image_label_1)[0]< -WIN_WIDTH:
#         canvas.coords(background_image_label_1, WIN_WIDTH, 0)
#     elif canvas.coords(background_image_label_2)[0]< -WIN_WIDTH:
#         canvas.coords(background_image_label_2, WIN_WIDTH, 0)
#     canvas.after(5, scroll_bg_image)

# scroll_bg_image()

# canvas.pack(expand=True, fill='both')
# frame.pack(expand=True, fill='both')
# root.bind('<Up>', move_up)
# root.bind('<Down>', move_down)
# root.bind('<Left>', move_left)
# root.bind('<Right>', move_right)
# root.mainloop()



from tkinter import Tk, Canvas, PhotoImage
from random import randint
from PIL import ImageTk, Image

# Create the Tkinter window
root = Tk()
root.title("Fruit Catcher")

# Create the canvas
canvas_width = 1400
canvas_height = 600
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()
class Fruit:
    def __init__(self):
        self.x = randint(200, canvas_width - 100)
        self.y = 0
        self.speed = randint(1, 5)
        self.image = PhotoImage(file="image 115.png")  # Replace "fruit.png" with your fruit image file

    def draw(self):
        canvas.create_image(self.x, self.y, anchor="center", image=self.image)

    def update(self):
        self.y += self.speed
        self.draw()
fruits = []

def create_fruit():
    fruit = Fruit()
    fruits.append(fruit)

def update_fruits():
    for fruit in fruits:
        fruit.update()

    # Remove fruits that have fallen off the screen
fruits[:] = [fruit for fruit in fruits if fruit.y < canvas_height]

    # Schedule the next fruit creation and update
canvas.after(1000, create_fruit)
canvas.after(50, update_fruits)
player_x = canvas_width // 2
player_y = canvas_height - 100
player_image = PhotoImage(file="img/cat.png")  # Replace "player.png" with your player image file

def draw_player():
    canvas.create_image(player_x, player_y, anchor="center", image=player_image)

def move_left(event):
    global player_x
    player_x -= 20
    if player_x < 0:
        player_x = 0
    draw_player()

def move_right(event):
    global player_x
    player_x += 20
    if player_x > canvas_width:
        player_x = canvas_width
    draw_player()

# Bind left and right arrow keys to player movement
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
create_fruit()
update_fruits()
draw_player()

root.mainloop()