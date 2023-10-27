import tkinter as tk
from PIL import Image, ImageTk
import random
WIN_WIDTH = 1350
WIN_HEIGHT = 750
SCROLLING_SPEED = 5


root = tk.Tk()
root.geometry(str(WIN_WIDTH) + "x" + str(WIN_HEIGHT))
frame = tk.Frame()
canvas = tk.Canvas(frame)


#__________background img_________
original_image = Image.open("bgwebp.jpg")
image_resize = original_image.resize((WIN_WIDTH, WIN_HEIGHT))
background_image = ImageTk.PhotoImage(image_resize)



#___________eat__________
apple_img1 =Image.open("apple(1).png")
image_resize_apple=apple_img1.resize((50, 50))
apple_photo=ImageTk.PhotoImage(image_resize_apple)

banana_img2 =Image.open("image-banana.png")
image_resize_banana=banana_img2.resize((50, 50))
banana_photo=ImageTk.PhotoImage(image_resize_banana)

strawberry_img3 =Image.open("image-strawberry.png")
image_resize_strawberry=strawberry_img3.resize((30, 30))
strawberry_photo=ImageTk.PhotoImage(image_resize_strawberry)

mango_img = Image.open("mango.png")
image_resize_mango=mango_img.resize((30, 30))
mango_photo=ImageTk.PhotoImage(image_resize_mango)

watermelon_img = Image.open("watermelon.png")
image_resize_watermelon=watermelon_img.resize((30, 30))
watermelon_photo=ImageTk.PhotoImage(image_resize_watermelon)

#_____________failure__________
bombpng_img3 =Image.open("image-bombpng.png")
image_resize_bombpng=bombpng_img3.resize((50, 50))
bombpng_photo=ImageTk.PhotoImage(image_resize_bombpng)


background_image_label_1= canvas.create_image(0, 0,anchor=tk.NW, image=background_image)
background_image_label_2= canvas.create_image(WIN_WIDTH,0,anchor=tk.NW, image=background_image)

background_image_label_A1= canvas.create_image(0, 0,anchor=tk.NW, image=apple_photo)
background_image_label_A2= canvas.create_image(0, 0,anchor=tk.NW, image=apple_photo)
background_image_label_A3= canvas.create_image(0, 0,anchor=tk.NW, image=apple_photo)
background_image_label_A4= canvas.create_image(0, 0,anchor=tk.NW, image=apple_photo)
background_image_label_A5= canvas.create_image(0, 0,anchor=tk.NW, image=apple_photo)
background_image_label_A6= canvas.create_image(0, 0,anchor=tk.NW, image=apple_photo)
background_image_label_A7= canvas.create_image(0, 0,anchor=tk.NW, image=apple_photo)
background_image_label_A8= canvas.create_image(0, 0,anchor=tk.NW, image=apple_photo)

background_image_label_B1= canvas.create_image(0, 0,anchor=tk.NW, image=bombpng_photo)
background_image_label_B2= canvas.create_image(0, 0,anchor=tk.NW, image=bombpng_photo)
background_image_label_B3= canvas.create_image(0, 0,anchor=tk.NW, image=bombpng_photo)
background_image_label_B4= canvas.create_image(0, 0,anchor=tk.NW, image=bombpng_photo)
background_image_label_B5= canvas.create_image(0, 0,anchor=tk.NW, image=bombpng_photo)
background_image_label_B6= canvas.create_image(0, 0,anchor=tk.NW, image=bombpng_photo)

background_image_label_C1= canvas.create_image(0, 0,anchor=tk.NW, image=banana_photo)
background_image_label_C2= canvas.create_image(0, 0,anchor=tk.NW, image=banana_photo)
background_image_label_C3= canvas.create_image(0, 0,anchor=tk.NW, image=banana_photo)

background_image_label_D1= canvas.create_image(0, 0,anchor=tk.NW, image=strawberry_photo)
background_image_label_D2= canvas.create_image(0, 0,anchor=tk.NW, image=strawberry_photo)
background_image_label_D3= canvas.create_image(0, 0,anchor=tk.NW, image=strawberry_photo)
background_image_label_D4= canvas.create_image(0, 0,anchor=tk.NW, image=strawberry_photo)
background_image_label_D5= canvas.create_image(0, 0,anchor=tk.NW, image=strawberry_photo)

background_image_label_E1= canvas.create_image(0, 0,anchor=tk.NW, image=mango_photo)
background_image_label_E2= canvas.create_image(0, 0,anchor=tk.NW, image=mango_photo)
background_image_label_E3= canvas.create_image(0, 0,anchor=tk.NW, image=mango_photo)


background_image_label_F1= canvas.create_image(0, 0,anchor=tk.NW, image=watermelon_photo)
background_image_label_F2= canvas.create_image(0, 0,anchor=tk.NW, image=watermelon_photo)
background_image_label_F3= canvas.create_image(0, 0,anchor=tk.NW, image=watermelon_photo)
background_image_label_F4= canvas.create_image(0, 0,anchor=tk.NW, image=watermelon_photo)


#___________player________
robot_image = Image.open("robot.png")
image_resize_robot = robot_image.resize((150, 150))
robot_photo = ImageTk.PhotoImage(image_resize_robot)

character = canvas.create_image(100, 600, image=robot_photo)

#_____________robot_______________

# def move_up(event):
#     canvas.move(character, 0, -10)

# def move_down(event):
#     canvas.move(character, 0, 10)

def move_left(event):
    canvas.move(character, -10, 0)

def move_right(event):
    canvas.move(character, 10, 0)

#____________bg__________
def scroll_bg_image():
    
    canvas.move(background_image_label_1, -1, 0)
    canvas.move(background_image_label_2, -1, 0)
#_______________apple_____
    canvas.move(background_image_label_A1, -1, 1)
    canvas.move(background_image_label_A2, -1, 1)
    canvas.move(background_image_label_A3, -1, 1)
    canvas.move(background_image_label_A4, -1, 1)
    canvas.move(background_image_label_A5, -1, 1)
    canvas.move(background_image_label_A6, -1, 1)
    canvas.move(background_image_label_A7, -1, 1)
    canvas.move(background_image_label_A8, -1, 1)
#_____________Bomb_____
    canvas.move(background_image_label_B1, -1, 1)
    canvas.move(background_image_label_B2, -1, 1)
    canvas.move(background_image_label_B3, -1, 1)
    canvas.move(background_image_label_B4, -1, 1)
    canvas.move(background_image_label_B5, -1, 1)
    canvas.move(background_image_label_B6, -1, 1)
#__________banana________
    canvas.move(background_image_label_C1, -1, 1)
    canvas.move(background_image_label_C2, -1, 1)
    canvas.move(background_image_label_C3, -1, 1)
#_______strawberry_______
    canvas.move(background_image_label_D1, -1, 1)
    canvas.move(background_image_label_D2, -1, 1)
    canvas.move(background_image_label_D3, -1, 1)
    canvas.move(background_image_label_D4, -1, 1)
    canvas.move(background_image_label_D5, -1, 1)
#_________mango______
    canvas.move(background_image_label_E1, -1, 1)
    canvas.move(background_image_label_E2, -1, 1)
    canvas.move(background_image_label_E3, -1, 1)
#_________watermelon______
    canvas.move(background_image_label_F1, -1, 1)
    canvas.move(background_image_label_F2, -1, 1)
    canvas.move(background_image_label_F3, -1, 1)
    canvas.move(background_image_label_F4, -1, 1)


    if canvas.coords(background_image_label_1)[0]< -WIN_WIDTH:
        canvas.coords(background_image_label_1, WIN_WIDTH, 0)
    elif canvas.coords(background_image_label_2)[0]< -WIN_WIDTH:
        canvas.coords(background_image_label_2, WIN_WIDTH, 0)

    elif canvas.coords(background_image_label_A1)[0]<0:
        canvas.coords(background_image_label_A1,1530,0)
    elif canvas.coords(background_image_label_A2)[0]<0:
        canvas.coords(background_image_label_A2,1560,0)
    elif canvas.coords(background_image_label_A3)[0]<0:
        canvas.coords(background_image_label_A3,1590,0)
    elif canvas.coords(background_image_label_A6)[0]<0:
        canvas.coords(background_image_label_A6,800,0)
    elif canvas.coords(background_image_label_A7)[0]<0:
        canvas.coords(background_image_label_A7,900,0)
    elif canvas.coords(background_image_label_A8)[0]<0:
        canvas.coords(background_image_label_A8,1000,0)

    elif canvas.coords(background_image_label_B1)[0]<0:
        canvas.coords(background_image_label_B1,1000,0)
    elif canvas.coords(background_image_label_B2)[0]<0:
        canvas.coords(background_image_label_B2,1500,0)
    elif canvas.coords(background_image_label_B3)[0]<0:
        canvas.coords(background_image_label_B3,1600,0)
    elif canvas.coords(background_image_label_B4)[0]<0:
        canvas.coords(background_image_label_B4,1700,0)
    elif canvas.coords(background_image_label_B5)[0]<0:
        canvas.coords(background_image_label_B5,1000,0)

    elif canvas.coords(background_image_label_C1)[0]<0:
        canvas.coords(background_image_label_C1,1800,0)
    elif canvas.coords(background_image_label_C2)[0]<0:
        canvas.coords(background_image_label_C2,2500,0)

    elif canvas.coords(background_image_label_D1)[0]<0:
        canvas.coords(background_image_label_D1,2000,0)
    elif canvas.coords(background_image_label_D2)[0]<0:
        canvas.coords(background_image_label_D2,2050,0)
    elif canvas.coords(background_image_label_D3)[0]<0:
        canvas.coords(background_image_label_D3,2100,0)


    elif canvas.coords(background_image_label_E1)[0]<0:
        canvas.coords(background_image_label_E1,1050,0)
    elif canvas.coords(background_image_label_E2)[0]<0:
        canvas.coords(background_image_label_E2,1100,0)
    elif canvas.coords(background_image_label_E3)[0]<0:
        canvas.coords(background_image_label_E3,1150,0)


    elif canvas.coords(background_image_label_F1)[0]<0:
        canvas.coords(background_image_label_F1,2500,0)
    elif canvas.coords(background_image_label_F2)[0]<0:
        canvas.coords(background_image_label_F2,2700,0)
    elif canvas.coords(background_image_label_F3)[0]<0:
        canvas.coords(background_image_label_F3,2900,0)
    elif canvas.coords(background_image_label_F4)[0]<0:
        canvas.coords(background_image_label_F4,3100,0)



    canvas.after(5, scroll_bg_image)

scroll_bg_image()


canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

# root.bind('<Up>', move_up)
# root.bind('<Down>', move_down)
root.bind('<Left>', move_left)
root.bind('<Right>', move_right)

root.mainloop()
