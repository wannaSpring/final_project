from tkinter import *
import time


def redraw():
    global gameMode
    if (gameMode == 1):
        cvs.move(player, pdx, pdy)
        if (playerCollideBorder()):
            gameMode = 2
    if (gameMode == 2):
        cvs.create_text(300, 100, fill="red", font="Times", text="Failed")


def mKeyEvent(event):
    global pdx
    global pdy
    global gameMode
    if (event.keysym == 'Up'):
        pdx = 0
        pdy = -speed
    if (event.keysym == 'Right'):
        pdx = speed
        pdy = 0
    if (event.keysym == 'Down'):
        pdx = 0
        pdy = speed
    if (event.keysym == 'Left'):
        pdx = -speed
        pdy = 0
    if (event.keysym == 'S' or event.keysym == 's'):
        gameMode = 1


def playerCollideBorder():
    x = cvs.coords(player)[0]
    y = cvs.coords(player)[1]
    collide = False
    if (x <= 0):
        collide = True
    if (x >= sWidth - 20):
        collide = True
    if (y <= 0):
        collide = True
    if (y >= sHeight - 20):
        collide = True
    return collide


tkw = Tk()
tkw.title("My Game program v1.0")
sWidth = 600
sHeight = 600
sBar = 50
px = sWidth / 2
py = sHeight - 50
pdx = 0
pdy = 0
speed = 10
gameMode = 0


cvs = Canvas(tkw, width=sWidth, height=sHeight + sBar)
cvs.create_rectangle(0, 0, sWidth, sHeight, fill="black")
cvs.create_rectangle(0, sHeight, sWidth, sHeight + sBar, fill="darkgreen")
player = cvs.create_rectangle(px, py, px + 20, py + 20, outline="cyan")
cvs.bind_all('<Key>', mKeyEvent)
cvs.pack()
while True:
    redraw()
    time.sleep(0.05)
    tkw.update()
cvs.mainloop;
