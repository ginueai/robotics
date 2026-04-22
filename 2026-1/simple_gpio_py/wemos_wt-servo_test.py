import machine
import dht
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
    
# D4 핀은 GPIO 2입니다.
sensor = dht.DHT22(machine.Pin(2))

def read_sensor():
    try:
        # 센서로부터 데이터 읽기 (최소 2초 간격 필요)
        sensor.measure()
        
        temp = sensor.temperature() # 온도 (°C)
        hum = sensor.humidity()    # 습도 (%)
        
        print(f"온도: {temp:.1f}°C, 습도: {hum:.1f}%")
        return (temp, hum)
        
    except OSError as e:
        print("센서 데이터를 읽는 데 실패했습니다. 연결을 확인하세요.")

# 무한 루프 테스트
try:
    print("AM2302(DHT22) 측정을 시작합니다...")
    while True:
        wt = read_sensor()
        if wt[1] > 30:
            print("정방향 회전")
            set_speed(50)
            time.sleep(2)
            set_speed(0)
        else:
            print("역방향 회전")
            set_speed(-50)
            time.sleep(2)
            set_speed(0)
            
        time.sleep(2) # 2초 대기

except KeyboardInterrupt:
    servo.deinit()
    print("중단됨")
