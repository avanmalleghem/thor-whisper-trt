import os

from launch import LaunchDescription
from launch_ros.actions import Node

ARGUMENTS = []

def generate_launch_description():

    speech_to_text_node = Node(
        package='speech_to_text',
        executable='speech_to_text_node.py',
    )

    # Launch them all!
    ld = LaunchDescription(ARGUMENTS)
    ld.add_action(speech_to_text_node)

    return ld