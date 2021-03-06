#!/bin/python3
# -*- coding: utf-8 -*-


# 라즈베리파이 GPIO 패키지 
import RPi.GPIO as GPIO
from time import sleep

# 모터 상태
STOP  = 0
FORWARD  = 1
BACKWARD = 2

# 모터 채널
CH1 = 0
CH2 = 1

# PIN 입출력 설정
OUTPUT = 1
INPUT = 0

# PIN 설정
HIGH = 1
LOW = 0

# 실제 핀 정의
#PWM PIN
ENA = 0   #27 pin
ENB = 26  #37 pin

#GPIO PIN
IN1 = 5  #37 pin
IN2 = 6  #35 pin
IN3 = 13   #31 pin
IN4 = 19   #29 pin

# 핀 설정 함수
def setPinConfig(EN, INA, INB):        
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)
    # 100khz 로 PWM 동작 시킴 
    pwm = GPIO.PWM(EN, 12) 
    # 우선 PWM 멈춤.   
    pwm.start(0) 
    return pwm

# 모터 제어 함수
def setMotorContorl(pwm, INA, INB, speed, stat):

    #모터 속도 제어 PWM
    pwm.ChangeDutyCycle(speed)  
    if stat == FORWARD:
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)
    #뒤로
    elif stat == BACKWARD:
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)
    #정지
    elif stat == STOP:
        GPIO.output(INA, LOW)
        GPIO.output(INB, LOW)

# 모터 제어함수 간단하게 사용하기 위해 한번더 래핑(감쌈)
def setMotor(ch, speed, stat):
    if ch == CH1:
        #pwmA는 핀 설정 후 pwm 핸들을 리턴 받은 값이다.
        setMotorContorl(pwmA, IN2, IN1, speed, stat)
    else:
        #pwmB는 핀 설정 후 pwm 핸들을 리턴 받은 값이다.
        setMotorContorl(pwmB, IN3, IN4, speed, stat)

# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)

#모터 핀 설정
#핀 설정후 PWM 핸들 얻어옴
pwmA = setPinConfig(ENA, IN1, IN2)
pwmB = setPinConfig(ENB, IN3, IN4)

#제어 시작

# 앞으로 80프로 속도로
setMotor(CH1, 80, BACKWARD)
setMotor(CH2, 80, BACKWARD)
#5초 대기
sleep(0.5)

#정지 
setMotor(CH1, 80, STOP)
setMotor(CH2, 80, STOP)

# 종료
GPIO.cleanup()
