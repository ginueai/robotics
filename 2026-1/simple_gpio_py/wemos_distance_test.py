import machine
import time

# 핀 설정
trig = machine.Pin(5, machine.Pin.OUT)
echo = machine.Pin(4, machine.Pin.IN)

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
            print(f"현재 거리: {dist} cm")
        else:
            print("범위 초과")
        time.sleep(1)

except KeyboardInterrupt:
    print("\n종료")