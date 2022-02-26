# TODO:1.missing import
# TODO:2.missing colon
def redraw()
    global gameMode
    if (gameMode == 1):
        # TODO: 3.pdx , pdy need global
        cvs.move(player, pdx, pdy)
        # TODO: 4.missing def playerCollideBorder
        if (playerCollideBorder())
            gameMode = 2
    #  TODO:5.Assignment symbols
    if (gameMode = 2):
        # TODO: 6.mssing comma
        cvs.create_text(300 100, fill="red", font="Times", text="Failed")
tkw = Tk()
#  TODO: 7. _ change ,
#    TDOO: 8. String not closed
tkw_title("My Game program v1.0)
sWidth = 600
sHeight = 600
sBar = 50
px = sWidth / 2
py = sHeight - 50
pdx = 0
pdy = 0
speed = 10
gameMode = 0
# TODO: 9.no tk, use tkw
cvs = Canvas(tk, width=sWidth, height=sHeight + sBar)
cvs.create_rectangle(0, 0, sWidth, sHeight, fill="black"):
cvs.create_rectangle(0, sHeight, sWidth, sHeight + sBar, fill="darkgreen")
# TODO: 10. mssing position y
# TODO: 11. Assignment symbols
player == cvs.create_rectangle(px, py, px + 20, outline="cyan")
# TODO: 12.missing def mKeyEvent
cvs.bind_all('<Key>', mKeyEvent)
# TODO: 13.the semi
cvs.pack():
# TODO: 14.true
while true:
    redraw()
    # TODO: 15. time.sleep
    sleep(0.05)
    tkw.update()
cvs.mainloop;