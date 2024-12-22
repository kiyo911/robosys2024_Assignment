import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "person", 10)
n = 0


def cb():
    global n
    msg = Person()
    msg.name = "清川広夢"
    msg.age = n
    pub.publish(msg)
    n += 1


def main():
    node.create_timer(0.5, cb)
    rclpy.spin(node)
