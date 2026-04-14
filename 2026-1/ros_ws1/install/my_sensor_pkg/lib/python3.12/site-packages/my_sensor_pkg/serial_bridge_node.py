import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String
import serial

class SerialBridgeNode(Node):
    def __init__(self):
        super().__init__('serial_bridge_node')
        
        # 1. Publisher: 거리 데이터 전송용
        self.publisher_ = self.create_publisher(Float32, 'sensor_distance', 10)
        
        # 2. Subscriber: 서보 제어 명령 수신용
        self.subscription = self.create_subscription(
            String, 'servo_command', self.servo_cmd_callback, 10)
        
        # 시리얼 포트 설정
        self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.1)
        
        # 시리얼 읽기 타이머 (10Hz)
        self.timer = self.create_timer(0.1, self.read_serial_timer_callback)

    def read_serial_timer_callback(self):
        """보드에서 오는 거리 데이터를 읽어 토픽으로 발행"""
        if self.ser.in_waiting > 0:
            try:
                line = self.ser.readline().decode('utf-8').strip()
                if line:
                    msg = Float32()
                    msg.data = float(line)
                    self.publisher_.publish(msg)
            except (ValueError, UnicodeDecodeError):
                pass

    def servo_cmd_callback(self, msg):
        """다른 노드에서 온 서보 명령을 시리얼로 보드에 전달"""
        command = msg.data # "MOVE" 또는 "STOP"
        self.get_logger().info(f'Sending to Arduino: {command}')
        self.ser.write(f"{command}\n".encode('utf-8'))

def main(args=None):
    rclpy.init(args=args)
    node = SerialBridgeNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
