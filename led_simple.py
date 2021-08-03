import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 8)

pixels[0] = (255, 0, 0)
pixels[2] = (0, 0, 255)
pixels[4] = (255, 255, 0)
pixels[5] = (0, 255, 0)


pixels.show



