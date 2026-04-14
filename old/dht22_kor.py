import time
import board
import adafruit_dht
dhtDevice = adafruit_dht.DHT22(board.D4)

temperature_c = dhtDevice.temperature
humidity = dhtDevice.humidity
print("현재 실내 온도는 / {:.1f}도 C 이고, 습도는 {}% 입니다.".format(temperature_c, humidity))

