import machine
import dht
import time

# D4 핀은 GPIO 2입니다.
sensor = dht.DHT22(machine.Pin(2))

def read_sensor():
    try:
        # 센서로부터 데이터 읽기 (최소 2초 간격 필요)
        sensor.measure()
        
        temp = sensor.temperature() # 온도 (°C)
        hum = sensor.humidity()    # 습도 (%)
        
        print(f"온도: {temp:.1f}°C, 습도: {hum:.1f}%")
        
    except OSError as e:
        print("센서 데이터를 읽는 데 실패했습니다. 연결을 확인하세요.")

# 무한 루프 테스트
try:
    print("AM2302(DHT22) 측정을 시작합니다...")
    while True:
        read_sensor()
        time.sleep(2) # 2초 대기

except KeyboardInterrupt:
    print("중단됨")