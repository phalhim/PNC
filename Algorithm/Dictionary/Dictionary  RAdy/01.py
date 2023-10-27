import tkinter as tk
#pip install pillow
from PIL import Image, ImageTk 
window =tk.Tk()
window.title("My window")
window.geometry("600x600")

# frame
frame = tk.Frame(window, width=600, height=600)
frame.pack()
# canvas
canvas =tk.Canvas(frame)
canvas.pack(pady=10)
canvas.create_rectangle(0,0,100,100,fill="yellow")
canvas.create_rectangle(500,0,600,100,fill="black")
canvas.create_rectangle(0,500,100,600,fill="pink")
canvas.create_rectangle(500,500,600,600,fill="green")
canvas.create_rectangle(400,200,200,300,fill="blue")

header1_id = canvas.create_text(300,150,text="Yoyo",font=("bold",50),fill="blue")
header2_id = canvas.create_text(300,350,text="Yoyo",font=("bold",50),fill="#EE05FF")

# Image 1
image_1 =Image.open("bacelona.png")
image_size =image_1.resize((200,400))
show_image_1 =ImageTk.PhotoImage(image_size)
img1_id = canvas.create_image(130,250,image=show_image_1)

# # Image_2
image_2 =Image.open("bayern.png")
image_size_2 =image_2.resize((100,100))
show_image_2 =ImageTk.PhotoImage(image_size_2)
img2_id = canvas.create_image(480,250,image=show_image_2)
def actionOne():
    canvas.itemconfigure(img1_id,image=show_image_2)
    canvas.itemconfigure(header1_id,fill="purple")
    canvas.itemconfigure(header2_id,fill="orange")
def actionTwo():
    canvas.itemconfigure(img2_id,image=show_image_1)
    canvas.itemconfigure(header1_id,fill="blue")
    canvas.itemconfigure(header2_id,fill="pink")

# move
def moveBacelona(event):
    print(canvas.coords(img1_id))
    if event.keysym == "Up" and canvas.coords(img1_id)[1]>50:
        x =0
        y=-10
        canvas.move(img1_id,x,y) 
    elif event.keysym=="Right" and canvas.coords(img1_id)[0]<560:
        x =10
        y=0
        canvas.move(img1_id,x,y)
    elif event.keysym=="Left" and canvas.coords(img1_id)[0] > 30:
        x =-10
        y=0
        canvas.move(img1_id,x,y)
    elif event.keysym=="Down" and canvas.coords(img1_id)[1]<540:
        x =0
        y=10
        canvas.move(img1_id,x,y)
def moveBayern(event):
    print(canvas.coords(img2_id))
    if event.keysym == "a" and canvas.coords(img2_id)[0]>30:
        x=0
        y=10
        canvas.move(img2_id,x,y)

# button 1
btn_1 =tk.Button(frame,text="Button One",command=actionOne)
btn_1.place(x=350,y=450)

#button 2
btn_2=tk.Button(frame,text="button Two",command=actionTwo)
btn_2.place(x=150,y=450)

window.bind("<Key>",moveBacelona)
window.mainloop()