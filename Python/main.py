import mandelbrot as mand
from PIL import Image

width = 1280
height = 720

scale = 2

def pixelToCoord( pos ):
    (x, y) = pos
    return ( 4*(x/height - 0.5)/scale ,  -4*(y/height - 0.5)/scale)


def main():
    me = mand.mandelbrot(2)
    img = Image.new('RGB', (width,height), color = 'white')
    for y in range(0, height):
        for x in range(0,width):
            c = pixelToCoord((x,y))
            if(me.isInSet(complex(c[0], c[1]), 1024)):
                img.putpixel((x,y), (0,0,0))
        if y%25 == 0:
            print("Row " + str(y))
    img.save("output2.png")

if __name__ == "__main__":
    main()
