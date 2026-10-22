import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class IzleyiciNode(Node):
    def __init__(self):
        super().__init__('izleyici')
        self.declare_parameter('esik', 30.0)
        self.subscription = self.create_subscription(
            Float32, '/sicaklik', self.dinle, 10)

    def dinle(self, msg):
        esik = self.get_parameter('esik').value
        if msg.data > esik:
            self.get_logger().warn(f'Yuksek sicaklik: {msg.data:.2f} (esik {esik})')
        else:
            self.get_logger().info(f'Sicaklik: {msg.data:.2f}')


def main(args=None):
    rclpy.init(args=args)
    node = IzleyiciNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()