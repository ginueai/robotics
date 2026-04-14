import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class DistanceSubscriber(Node):
    def __init__(self):
        super().__init__('distance_subscriber')
        self.subscription = self.create_subscription(
            Float32, 'sensor_distance', self.listener_callback, 10)

    def listener_callback(self, msg):
        dist = msg.data
        if dist < 10.0:
            self.get_logger().warn(f"너무 가까움! 위험! ({dist:.1f} cm)")
        elif dist < 30.0:
            self.get_logger().info(f"주의: 장애물 감지 ({dist:.1f} cm)")
        else:
            self.get_logger().info(f"안전 거리 ({dist:.1f} cm)")

def main(args=None):
    rclpy.init(args=args)
    node = DistanceSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
