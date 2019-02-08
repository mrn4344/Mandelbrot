import mandelbrot as mand
import imaginary as im
from PIL import Image
#import turtle as t
#import math

width = 1600
height = 900

scale = 2


def init():
    t.setup(width, height, 1, 1)
    t.title("Mandelbrot Viewer")
    t.screensize(width, height, "white")
    t.setworldcoordinates(0, height, width, 0)
    t.tracer(0,1)
    t.hideturtle()
    t.pensize(1)
    t.seth(90)

def drawPixel(pos, color):
    #t.up()
    t.goto(pos)
    t.pencolor(color)
    #t.pd()
    #t.fd(1)
    t.goto(pos[0]+1, pos[1])

def magnitude(c):
    return math.sqrt(c[0]*c[0]+c[1]*c[1])

def function(z, c):
    return ( ((z[0]*z[0]) - (z[1]*z[1])) + c[0] , (2*z[0]*z[1]) + c[1])

def inMandelbrot(c):
    number = (0,0)
    for i in range(0, 128):
        number = function(number, c)
        if magnitude(number) > 2:
            return False
    return True

def pixelToCoord( pos ):
    (x, y) = pos
    return ( (1/(225*scale))*(x - width/2) , (1/(scale*225))*(height/2 - y) )


def main():
    me = mand.mandelbrot(2)
    img = Image.new('RGB', (1920,1080), color = 'white')
    #values = [([None] * height)] * width
    for y in range(0, height):
        for x in range(0,width):
            c = pixelToCoord((x,y))
            if(me.isInSet(complex(c[0], c[1]), 1024)):
                img.putpixel((x,y), (0,0,0))
        print("Row " + str(y))
            #print("Trying point" + str(c))
            #if inMandelbrot(c):
            #    drawPixel( (x,y), (0,0,0))
            #else:
            #    drawPixel( (x,y), '#ff0000')
    img.save("output1.png")
        #t.update()
    # t.goto(0,0)
    # t.pd()
    # t.goto(1600,0)
    # t.up()
    # t.pencolor("red")
    # t.goto(0,1)
    # t.pd()
    # t.goto(1600,1)
    #t.update()
    #t.exitonclick()

if __name__ == "__main__":
    main()
