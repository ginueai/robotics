import machine
import time

# D5 핀 (GPIO 14) 설정
servo_pin = machine.Pin(14)
servo = machine.PWM(servo_pin, freq=50)

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

try:
    print("360도 서보 테스트 시작")
    
    # 1. 정지 (중립점 찾기)
    # 만약 0인데도 모터가 천천히 돈다면 duty_val 계산식의 77을 76이나 78로 미세조정하세요.
    print("정지")
    set_speed(0)
    time.sleep(2)

    # 2. 정방향 서서히 가속
    print("정방향 회전")
    set_speed(50)
    time.sleep(2)
    set_speed(100)
    time.sleep(2)

    # 3. 역방향 회전
    print("역방향 회전")
    set_speed(-50)
    time.sleep(2)
    set_speed(-100)
    time.sleep(2)

    # 4. 종료 전 정지
    set_speed(0)

except KeyboardInterrupt:
    servo.deinit()
    print("종료")