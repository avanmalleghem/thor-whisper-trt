#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class SpeechToText(Node):
    def __init__(self):
        super().__init__('speech_to_text_node')

        self.get_logger().info('Started!')

def main(args=None):
    # init the node
    rclpy.init(args=args)
    speech_to_text_node = SpeechToText()
    # spin() simply keeps python from exiting until this node is stopped
    rclpy.spin(speech_to_text_node)
    speech_to_text_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
