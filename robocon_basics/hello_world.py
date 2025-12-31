import rclpy
from rclpy.node import Node
from std_msgs.msg import  String

class Mynode(Node):
    def __init__(self):
        super().__init__("hello_world")

        self.publisher = self.create_publisher(String, 'topic',10)
        self.create_timer(0.5, self.printer)
        self.i = 0

    def printer(self):
        msg = String()
        msg.data = "Hello World"
        self.publisher.publish(msg)
        self.get_logger().info('You say:%s %d' % (msg.data, self.i) )
        self.i += 1
    


def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = Mynode()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()