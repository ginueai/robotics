import time
import subprocess

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
x = 0

def eye2():
    draw.rectangle((0, 0, width, height), outline=0, fill=0)    
    #draw eye
    draw.rectangle((24, 20, 50, 35), outline=1, fill=255)
    draw.rectangle((78, 20, 104, 35), outline=1, fill=255)
    # Display image.
    disp.image(image)
    disp.show()
    time.sleep(0.1)

#while True:
eye2()
