from microbit import *

# 서보모터 초기 설정 (P0 핀, 주기 20ms)
pin0.set_analog_period(20)

while True:
    # 1. 빛 센서 값 읽기 (0 ~ 255)
    light_level = display.read_light_level()
    
    # 2. 센서 값을 서보 각도(PWM 듀티)로 변환 (Mapping)
    # 빛(0~255) -> 서보(26~128)
    # 계산식: 최소값 + (입력값 * 범위비율)
    if light_level < 50:
        servo_value = int(26 + (50 * (102 / 255)))
    else:
        servo_value = 100
    
    # 3. 서보모터 제어
    pin0.write_analog(servo_value)
    
    # 4. 현재 빛의 양을 LED 숫자로 잠깐 표시 (디버깅용)
    # 너무 자주 출력하면 모터가 떨리므로 생략하거나 짧게 조절
    # display.scroll(str(light_level), delay=50) 
    
    sleep(100) # 0.1초마다 갱신