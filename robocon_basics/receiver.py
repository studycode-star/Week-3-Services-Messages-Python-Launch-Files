import rclpy
from rclpy.node import Node
from std_msgs.msg import  String

class Mynode(Node):
    def __init__(self):
        super().__init__("receiver")
        self.subscriber = self.create_subscription(
            String,
            'topic',
            self.callback,
            10,
        )
    
    def callback(self, msg):
        self.get_logger().info(msg.data)

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = Mynode()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()