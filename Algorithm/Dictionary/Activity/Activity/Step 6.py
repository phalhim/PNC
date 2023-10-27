import tkinter as tk

def button_clicked():
    print("Button Clicked!")

window = tk.Tk()
window.geometry('500x500')
frame = tk.Frame(window, width=500, height=500)
frame.pack()

canvas = tk.Canvas(frame, width=500, height=500)
canvas.pack()

ball = canvas.create_oval(190, 190, 210, 210, fill="green")
wall = canvas.create_rectangle(300, 50, 320, 300, fill="black", tags="wall")

# Define the step size for movement
step_size = 10

def changeball(event):
    ball_coords = canvas.coords(ball)
    if event.keysym == "Right":
        new_coords = [ball_coords[0] + step_size, ball_coords[1], ball_coords[2] + step_size, ball_coords[3]]
        if not is_collision(new_coords, canvas.coords(wall)):
            canvas.move(ball, step_size, 0)
    elif event.keysym == "Left":
        new_coords = [ball_coords[0] - step_size, ball_coords[1], ball_coords[2] - step_size, ball_coords[3]]
        if not is_collision(new_coords, canvas.coords(wall)):
            canvas.move(ball, -step_size, 0)
    elif event.keysym == "Up":
        new_coords = [ball_coords[0], ball_coords[1] - step_size, ball_coords[2], ball_coords[3] - step_size]
        if not is_collision(new_coords, canvas.coords(wall)):
            canvas.move(ball, 0, -step_size)
    elif event.keysym == "Down":
        new_coords = [ball_coords[0], ball_coords[1] + step_size, ball_coords[2], ball_coords[3] + step_size]
        if not is_collision(new_coords, canvas.coords(wall)):
            canvas.move(ball, 0, step_size)

def is_collision(ball, wall):
    return ball[2] >= wall[0] and ball[3] >= wall[1] and ball[0] <= wall[2] and ball[1] <= wall[3]

window.bind("<Key>", changeball)

window.mainloop()
