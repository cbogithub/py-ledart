# import all patterns availble for use.
from Ledart.Patterns.Patterns import *

pixelmatrix = "Arduino-42"
ledboard = 'ledboard'
minimatrix = 'minimatrix'
megamatrix = 'megamatrix'
localhost = "127.0.0.1"
bcast = '10.42.0.0'
moo = 'moo'
dest = megamatrix
# dest = minimatrix
# dest = moo
# dest = localhost
# dest = ledboard
# dest = pixelmatrix
# dest = localhost
# dest = '10.42.3.12'
# dest = '10.42.7.124'
# dest = '10.42.4.84'
# dest = '10.42.6.105'
# dest = '10.42.4.12'

TARGETS = {
    # dest: RainPattern(color=(0xff, 0xff, 0xff), chance=0.5),
    # dest: FillTest(),
    # dest: Sven(),
    # dest: BarberpolePattern(),
    # dest: OldTron(),
    # dest: Tron(),
    # dest: Snake(speed=17),
    # dest: MixedLife(),
    # dest: ProgressedLife(decay=30),
    # dest: GraphicsLineScroll(),
    # dest: RandomLife(),
    # dest: Mandelbrot(),
    # dest: Sim(),
    # dest: PixelLife(color=(0, 0, 0xFF)),
    # dest: SuperPixelBros(),
    # dest: Pong(speed=5),
    # dest: Pong(bcolor=(0, 0, 255), speed=3, port="USB", plugged=0),
    # dest: Pong(speed=8),
    # dest: ScreenCapture(fullscreen=True),
    # dest: ScreenCapture(fullscreen=False),
    # dest: DisplayImage('Ledart/images/tkkrlab.png'),
    # dest: DisplayGif('/home/robert/1353.gif'),
    # dest: VideoPlay('/home/robert/Videos/bad-noshadow.mp4'),
    # dest: VideoPlay('/home/robert/Videos/bad.mkv'),
    # dest: VideoTest(),
    # dest: CamCapture(),
    # dest: Water(),
    # dest: AliasedWPlasma(),
    
    # dest: AliasedFire(),
    dest: MiniFire(),
    # dest: Smolders(),
    # dest: FireOne(),
    # dest: FireTwo(),
    # dest: FireThree(),
    # dest: RectTest(),

    # dest: RainbowEffect(),
    # dest: ColorFade(),
    # dest: PlasmaFifth(),
    # dest: PlasmaFourth(),
    # dest: PlasmaFirst(),
    # dest: PlasmaSecond(),
    # dest: PlasmaThird(),
    # dest: RevolvingCircle(),
    # dest: RainPattern(chance=0.7, color=(40, 60, 255)),
    # dest: GraphicsCircleTest(),
    # dest: GraphicsRectTest(),
    # dest: GraphicsLineTest(),
    # dest: GraphicsPixelTest(),
    # dest: GraphicsDotTest(),
    # dest: VUmeter(),
}
