
def myEventTrigger(events):
    print("Uesr clicks on circe : ", events.x, events.y)
def myEvent(events):
    print("Uesr clicks on square : ", events.x, events.y)
def Event(events):
    print("Uesr clicks on rectangl : ", events.x, events.y)


import tkinter as tk
root =tk.Tk()
root.geometry("600x600")
frame = tk.Frame()
frame.master.title("KK")
canvas =tk.Canvas(frame)

canvas.create_oval(50, 50, 300, 300, fill="red", tags="PNCTarget")
canvas.tag_bind("PNCTarget", "<Button-1>", myEventTrigger)
canvas.create_rectangle(80, 550, 550, 300, fill="blue", tags="PNCEvent")
canvas.tag_bind("PNCEvent", "<Button-1>", myEvent)
canvas.create_rectangle(400, 300, 550, 100, fill="black", tags="PNCCall")
canvas.tag_bind("PNCCall", "<Button-1>", Event)

canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")

root.mainloop()
