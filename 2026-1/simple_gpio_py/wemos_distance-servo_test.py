import machine
import time

# D5 핀 (GPIO 14) 설정
servo_pin = machine.Pin(14)
servo = machine.PWM(servo_pin, freq=50)

# 핀 설정
trig = machine.Pin(5, machine.Pin.OUT)
echo = machine.Pin(4, machine.Pin.IN)

def set_speed(speed):
    """
    speed: -100 (최대 역회전) ~ 100 (최대 정회전)
    0은 정지
    """
    # EF90D의 특성에 맞춘 매핑 (중립 약 77)
    # -100일 때 약 40, 0일 때 77, 100일 때 약 115
    duty_val = int(77 + (speed / 100 * 38))
    servo.duty(duty_val)
    print(f"Speed: {speed}, Duty: {duty_val}")
    
def get_distance():
    # 1. 초기화 (low 대신 value(0) 사용)
    trig.value(0)
    time.sleep_us(2)
    
    # 2. 10us 동안 초음파 발사 (high 대신 value(1) 사용)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    
    # 3. Echo 시간 측정
    duration = machine.time_pulse_us(echo, 1, 30000)
    
    if duration < 0:
        return None
        
    distance = (duration * 0.0343) / 2
    return round(distance, 1)

try:
    print("--- 초음파 센서 거리 측정 시작 ---")
    while True:
        dist = get_distance()
        if dist is not None:
            if dist > 30:
                set_speed(0)
            else:
                print("역방향 회전")
                set_speed(-50)
                time.sleep(2)
                set_speed(0)
                
            print(f"현재 거리: {dist} cm")
        else:
            print("범위 초과")
        time.sleep(1)
    
except KeyboardInterrupt:
    print("\n종료")