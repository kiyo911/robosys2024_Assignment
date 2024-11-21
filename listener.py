import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
n = 0


def cb(msg):
    global node
    node.get_logger().info("listen: %d" % msg.data)


def main():
    pub = node.create_subscription(Int16, "countup", cb, 10)
    rclpy.spin(node)