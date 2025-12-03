import os

from launch import LaunchDescription
from launch_ros.actions import Node

ARGUMENTS = []

def generate_launch_description():

    speech_to_text_node = Node(
        package='speech_to_text',
        executable='speech_to_text_node.py',
    )

    text_to_cmd_vel_node = Node(
        package='text_to_cmd_vel',
        executable='text_to_cmd_vel',
    )

    # Launch them all!
    ld = LaunchDescription(ARGUMENTS)
    ld.add_action(speech_to_text_node)
    ld.add_action(text_to_cmd_vel_node)

    return ld