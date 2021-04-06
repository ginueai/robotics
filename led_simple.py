import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 8)

pixels[0] = (255, 0, 0)
pixels[1] = (255, 255, 0)
pixels[7] = (0, 0, 255)
pixels[5] = (255, 255, 255)

pixels.show



