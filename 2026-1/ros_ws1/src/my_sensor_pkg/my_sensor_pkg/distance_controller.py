import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

class DistanceController(Node):
    def __init__(self):
        super().__init__('distance_controller')
        
        # 거리 토픽 구독
        self.subscription = self.create_subscription(
            Float32, 'sensor_distance', self.listener_callback, 10)
        
        # 서보 명령 토픽 발행
        self.publisher_ = self.create_publisher(String, 'servo_command', 10)

    def listener_callback(self, msg):
        dist = msg.data
        cmd_msg = String()
        
        if dist < 15.0:
            cmd_msg.data = "MOVE"
            self.get_logger().warn(f"장애물 감지 ({dist:.1f}cm)! MOVE 명령 전송")
        else:
            cmd_msg.data = "STOP"
            self.get_logger().info(f"거리 안전 ({dist:.1f}cm). STOP 명령 전송")
            
        self.publisher_.publish(cmd_msg)

def main(args=None):
    rclpy.init(args=args)
    node = DistanceController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
