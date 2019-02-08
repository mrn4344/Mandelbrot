import mandelbrot as mand
from PIL import Image

width = 1600
height = 900

scale = 2

def pixelToCoord( pos ):
    (x, y) = pos
    return ( (1/(225*scale))*(x - width/2) , (1/(scale*225))*(height/2 - y) )


def main():
    me = mand.mandelbrot(2)
    img = Image.new('RGB', (1920,1080), color = 'white')
    for y in range(0, height):
        for x in range(0,width):
            c = pixelToCoord((x,y))
            if(me.isInSet(complex(c[0], c[1]), 1024)):
                img.putpixel((x,y), (0,0,0))
        print("Row " + str(y))
    img.save("output1.png")

if __name__ == "__main__":
    main()
