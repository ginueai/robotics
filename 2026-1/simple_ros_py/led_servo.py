from machine import Pin, PWM
import time
# Wemos 내장 LED는 보통 GPIO 2번입니다.
led = Pin(4, Pin.OUT)

# D4(GPIO 2) 핀을 PWM 출력으로 설정
servo = PWM(Pin(5), freq=50) # 서보 모터는 보통 50Hz 사용

def set_servo_speed(duty):
    # duty 범위: 약 40(최대 역회전) ~ 77(정지) ~ 115(최대 정회전)
    # 실제 보드나 모터마다 정지점(Deadband)이 조금씩 다를 수 있습니다.
    servo.duty(duty)

try:
    print("정방향 회전")
    led.value(1) # 켜짐 확인
    set_servo_speed(100) 
    time.sleep(2)

    print("정지")
    led.value(0)
    set_servo_speed(77) # 모터가 미세하게 움직이면 75~78 사이에서 조정하세요.
    time.sleep(2)

    print("역방향 회전")
    led.value(1)
    set_servo_speed(50)
    time.sleep(2)
    led.value(0)

finally:
    servo.deinit() # PWM 해제
