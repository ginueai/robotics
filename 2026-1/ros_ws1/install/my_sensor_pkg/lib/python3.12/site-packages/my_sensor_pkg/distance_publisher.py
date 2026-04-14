import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import serial

class DistancePublisher(Node):
    def __init__(self):
        super().__init__('distance_publisher')
        self.publisher_ = self.create_publisher(Float32, 'sensor_distance', 10)
        # 시리얼 포트 설정 (포트 이름 주의)
        self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        if self.ser.in_waiting > 0:
            line = self.ser.readline().decode('utf-8').strip()
            try:
                distance_val = float(line)
                msg = Float32()
                msg.data = distance_val
                self.publisher_.publish(msg)
                self.get_logger().info(f'Publishing: {msg.data} cm')
            except ValueError:
                pass

def main(args=None):
    rclpy.init(args=args)
    node = DistancePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
