# -*- coding: utf-8 -*-

#------------------------
#oled code
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
# Move left to right keeping track of the current x position for drawing shapes.
x = 10

# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 9)
def disp_screen(string):
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Write four lines of text.
    draw.text((x, top + 10), string, font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.show()
    time.sleep(0.1)
#------------------------
import RPi.GPIO as GPIO
import time
import sys
import signal

#GPIO 핀
TRIG = 23 # 트리거
ECHO = 24 # 에코

#거리 타임 아웃 용
MAX_DISTANCE_CM = 300
MAX_DURATION_TIMEOUT = (MAX_DISTANCE_CM * 2 * 29.1) #17460 # 17460us = 300cm

# 키보드 CTRL + C 누르면 종료 되게 처리
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        GPIO.cleanup()
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

# cm 환산 함수
# 아두이노 UltraDistSensor 코드에서 가져옴
def distanceInCm(duration):
    # 물체에 도착후 돌아오는 시간 계산
    # 시간 = cm / 음속 * 왕복
    # t   = 0.01/340 * 2= 0.000058824초 (58.824us)

    # 인식까지의 시간
    # t = 0.01/340 = 0.000029412초 (29.412us)

    # duration은 왕복 시간이니 인식까지의 시간에서 2로 나눔
    return (duration/2)/29.1


# 거리 표시
def print_distance(distance):
    if distance == 0:
        distanceMsg = 'Distance : out of range                   \r'
    else:
        distanceMsg = 'Distance : ' + str(distance) + 'cm' + '        \r'
    sys.stdout.write(distanceMsg)
    sys.stdout.flush()


def main():
    # 파이썬 GPIO 모드
    GPIO.setmode(GPIO.BCM)

    # 핀 설정
    GPIO.setup(TRIG, GPIO.OUT) # 트리거 출력
    GPIO.setup(ECHO, GPIO.IN)  # 에코 입력

    print('To Exit, Press the CTRL+C Keys')

    # HC-SR04 시작 전 잠시 대기
    GPIO.output(TRIG, False)
    print('Waiting For Sensor To Ready')
    time.sleep(1) # 1초

    #시작
    print('Start!!')
    while True:
        #171206 중간에 통신 안되는 문제 개선용      
        fail = False
        time.sleep(0.1)
        # 트리거를 10us 동안 High 했다가 Low로 함.
        # sleep 0.00001 = 10us
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        # ECHO로 신호가 들어 올때까지 대기
        timeout = time.time()
        while GPIO.input(ECHO) == 0:
            #들어왔으면 시작 시간을 변수에 저장
            pulse_start = time.time()
            if ((pulse_start - timeout)*1000000) >= MAX_DURATION_TIMEOUT:
                #171206 중간에 통신 안되는 문제 개선용        
                #continue
                fail = True
                break
                
        #171206 중간에 통신 안되는 문제 개선용        
        if fail:
            continue
        #ECHO로 인식 종료 시점까지 대기
        timeout = time.time()
        while GPIO.input(ECHO) == 1:
            #종료 시간 변수에 저장
            pulse_end = time.time()
            if ((pulse_end - pulse_start)*1000000) >= MAX_DURATION_TIMEOUT:
                print_distance(0) 
                #171206 중간에 통신 안되는 문제 개선용        
                #continue
                fail = True
                break

        #171206 중간에 통신 안되는 문제 개선용        
        if fail:
            continue

        #인식 시작부터 종료까지의 차가 바로 거리 인식 시간
        pulse_duration = (pulse_end - pulse_start) * 1000000

        # 시간을 cm로 환산
        distance = distanceInCm(pulse_duration)
        #print(pulse_duration)
        #print('')
        # 자리수 반올림
        distance = round(distance, 2)

        #표시
        print_distance(distance)
        disp_screen(f'DISTANCE: {distance} cm')

    GPIO.cleanup()



if __name__ == '__main__':
    main()