from tkinter import Tk, Canvas, PhotoImage, mainloop
from math import sin

WIDTH, HEIGHT = 320,200
start_x, start_y = 0,0
window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#ffffff")
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")




def plot(x,y): # set pixel
    img.put("#000", (x,y))

def plotLineLow(x0, y0, x1, y1): # needed for left and right
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    else:
        D = (2 * dy) - dx
        y = y0

    for x in range(x0,x1):
        plot(x, y)
        if D > 0:
            y = y + yi
            D = D + (2 * (dy - dx))
        else:
            D = D + 2*dy

def plotLineHigh(x0, y0, x1, y1): # needed for up and down
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    else:
        D = (2 * dx) - dy
        x = x0

    for y in range(y0,y1):
        plot(x, y)
        if D > 0:
            x = x + xi
            D = D + (2 * (dx - dy))
        else:
            D = D + 2*dx

def plotLine(x0, y0, x1, y1): # lineto function
    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            plotLineLow(x1, y1, x0, y0)# right to left
            print("a")
        else:
            plotLineLow(x0, y0, x1, y1)# left to right
            print("b")
    else:
        if y0 > y1:
            plotLineHigh(x1, y1, x0, y0)#bottom to top
            print("c")
        else:
            plotLineHigh(x0, y0, x1, y1)# top to bottom
            print("d")

plotLine(100,50,200,50)

plotLine(200,50,200,150)

plotLine(200,150,100,150)

plotLine(100,150,100,50)

mainloop()

#moveto(100, 50)
#lineto(200, 50)
#lineto(200, 150)
#lineto(100, 150)
#lineto(100, 50)
