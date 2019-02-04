import turtle as t

width = 1600
height = 900

def init():
    t.setup(width, height, 1, 1)
    t.title("Mandelbrot Viewer")
    t.screensize(width, height, "white")
    t.setworldcoordinates(0, height, width, 0)
    t.tracer(0,1)
    t.hideturtle()
    t.pensize(1)

def drawPixel(pos, color):
    t.up()
    t.goto(pos)
    t.pencolor(color)
    t.pd()
    t.goto(pos[0]+1, pos[1])
    t.up()

def function(z, c):
    return ( ((z[0]*z[0]) - (z[1]*z[1])) + c[0] , (2*z[0]*z[1]) + c[1])

def inMandelbrot(c):
    number = (0,0)
    for i in range(0, 1024):
        number = function(number, c)
        if Math.sqrt(number[0]*number[0] + number[1]*number[1]) > 2:
            return False
    return True

def pixelToCoord(pos):
    return



def main():
    init()
    drawPixel((0,0), "red")
    drawPixel((1,0), "green")
    drawPixel((2,0), "blue")
    # t.goto(0,0)
    # t.pd()
    # t.goto(1600,0)
    # t.up()
    # t.pencolor("red")
    # t.goto(0,1)
    # t.pd()
    # t.goto(1600,1)
    t.update()
    t.exitonclick()

if __name__ == "__main__":
    main()
