import time
import sys
from Pixel import Pixel
import Graphics.Graphics as Graphics
import matrix
from Interfaces import OpenGlInterface, PygameInterface

interface_opts = {
    "pygame": PygameInterface,
    "opengl": OpenGlInterface,
}


class MatrixScreen(object):
    """
    this module/class is a matrix simulator (led)
    it draws blocks in a array the size of the pixels is
    defined in matrix.py
    """
    def __init__(self, width, height, pixelsize, fullscreen=False,
                 interface=OpenGlInterface):
        self.interface = interface(width, height, pixelsize, fullscreen)
        self.width = width
        self.height = height
        self.pixelSize = pixelsize

        self.pixels = []

        self.window_width = height * pixelsize
        self.window_height = width * pixelsize

        self.interface.setcaption("pygame artnet matrix simulator.")

        widthrange = range(0, self.window_width, pixelsize)
        # reverse order because else the display is flipped.
        heightrange = range(0, self.window_height, pixelsize)[::-1]

        # due to how the ledmatrix is displayed x, y are filled as is the
        # window_width/height thing a bit above here.
        for x in widthrange:
            for y in heightrange:
                pos = (x, y)
                color = Graphics.BLUE
                pixel = Pixel(pos, pixelsize, color)
                self.pixels.append(pixel)

        # for keeping fps
        self.previous = 1
        self.time = 1
        self.fps = 0

    def handleinput(self):
        self.interface.handleinput()

    def draw(self, data):
        # extract pixels and color from data
        # get both a list index and the color data.
        for i, color in enumerate(data):
            self.pixels[i].setColor(color)
        # clear the window
        self.interface.clear(Graphics.BLACK)
        # display the pixels.
        for pixel in self.pixels:
            r = pixel.color[matrix.COLOR_ORDER[0]]
            g = pixel.color[matrix.COLOR_ORDER[1]]
            b = pixel.color[matrix.COLOR_ORDER[2]]
            color = (r, g, b)
            # for a nice litle border that makes the pixels stand out.
            bordercolor = Graphics.BLACK
            self.interface.drawblock(pixel.getRect(), color, bordercolor)

        # update the screen so our data show.
        self.interface.update()

    def process(self, data):
        self.time = time.time()
        self.fps = 1. / (self.time - self.previous)
        self.previous = self.time
        self.interface.setcaption("artnet matrix sim FPS:" +
                                  str(int(self.fps)))
        self.handleinput()
        self.draw(data)

    def printfps(self):
        sys.stdout.write("%s      \r" % self.fps)

    def __del__(self):
        self.interface.quit()
