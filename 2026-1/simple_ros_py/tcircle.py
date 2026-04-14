import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CircleMover(Node):
    def __init__(self):
        super().__init__('circle_mover_node')
        # 퍼블리셔 생성: 'turtle1/cmd_vel' 토픽에 Twist 메시지 전송
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        
        # 0.1초마다 timer_callback 함수 실행
        timer_period = 0.1  
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        # 선속도: 앞으로 가는 힘 (1.0 m/s)
        msg.linear.x = 2.0
        # 각속도: 회전하는 힘 (1.0 rad/s)
        # 선속도와 각속도가 일정하면 원을 그리게 됩니다.
        msg.angular.z = 1.0
        
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: linear.x=%f, angular.z=%f' % (msg.linear.x, msg.angular.z))

def main(args=None):
    rclpy.init(args=args)
    circle_mover = CircleMover()
    
    try:
        rclpy.spin(circle_mover)
    except KeyboardInterrupt:
        # 종료 시 거북이를 멈추기 위해 속도 0 전송
        stop_msg = Twist()
        circle_mover.publisher_.publish(stop_msg)
        circle_mover.get_logger().info('Node stopped cleanly')
    finally:
        circle_mover.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
