#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped

def main(args=None):
    rclpy.init(args=args)
    node = Node("relay")
    pub = node.create_publisher(AckermannDriveStamped, 'drive_relay', 10)

    def callback(msg):
        new = AckermannDriveStamped()
        new.header = msg.header
        new.drive.speed = msg.drive.speed * 3.0
        new.drive.steering_angle = msg.drive.steering_angle * 3.0
        node.get_logger().info(f"Relaying: v={new.drive.speed}, d={new.drive.steering_angle}")
        pub.publish(new)

    node.create_subscription(AckermannDriveStamped, 'drive', callback, 10)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
