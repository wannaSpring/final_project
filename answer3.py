
def redraw()
    global gameMode
    if (gameMode == 1):
        cvs.move(player, pdx, pdy) if (playerCollideBorder())
    gameMode = 2
    if (gameMode = 2):
        cvs.create_text(300,100, fill = "red", font = "Times", text = "Failed")
    tkw = Tk()
    tkw_title("My Game program v1.0) sWidth = 600 sHeight = 600 sBar = 50 px = sWidth / 2 py = sHeight - 50 pdx = 0 pdy = 0 speed = 10 gameMode = 0
    cvs = Canvas(tk, width=sWidth, height=sHeight + sBar)
    cvs.create_rectangle(0, 0, sWidth, sHeight, fill="black"):
    cvs.create_rectangle(0, sHeight, sWidth, sHeight + sBar,fill="darkgreen")
    player == cvs.create_rectangle(px, py, px + 20, outline="cyan")
    cvs.bind_all('<Key>', mKeyEvent)
    cvs.pack():
    while true:     redraw()
    sleep(0.05)
    tkw.update()
    cvs.mainloop;
