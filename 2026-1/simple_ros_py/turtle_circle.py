import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist # 거북이 속도 메시지 타입

class TurtleCirclePublisher(Node):
    def __init__(self):
        # 1. 노드 이름 초기화
        super().__init__('turtle_circle_publisher')
        
        # 2. 퍼블리셔 생성 (토픽명: /turtle1/cmd_vel, 큐 사이즈: 10)
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        # 3. 타이머 생성 (0.1초마다 timer_callback 함수 실행 -> 10Hz)
        timer_period = 0.1  
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # 4. 메시지 객체 생성 및 값 대입
        msg = Twist()
        msg.linear.x = 2.0  # 전진 속도
        msg.angular.z = 1.0 # 회전 속도 (좌회전)
        
        # 5. 메시지 발행
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: Linear={msg.linear.x}, Angular={msg.angular.z}')

def main(args=None):
    rclpy.init(args=args)
    node = TurtleCirclePublisher()
    try:
        rclpy.spin(node) # 노드를 계속 실행 상태로 유지
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
