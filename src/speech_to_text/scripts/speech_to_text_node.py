#!/usr/bin/env python3

import rclpy
import time
from std_msgs.msg import String
from rclpy.node import Node

from whisper_trt import load_trt_model

class SpeechToText(Node):
    def __init__(self):
        super().__init__('speech_to_text_node')

        self.model = load_trt_model("base.en")

        self.subscription = self.create_subscription(
            String,
            'speech_path',
            self.listener_callback,
            1)
        self.subscription  # prevent unused variable warning

        self.publisher = self.create_publisher(String, 'text', 1)

        self.get_logger().info('Started!')

    def listener_callback(self, msg):
        t0 = time.time()
        result = self.model.transcribe(msg.data)['text']
        t1 = time.time()
        total = t1-t0
        self.get_logger().info(f"Transcription of {msg.data} took {total} seconds")

        text_msg = String()
        text_msg.data = result
        self.publisher.publish(text_msg)

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
