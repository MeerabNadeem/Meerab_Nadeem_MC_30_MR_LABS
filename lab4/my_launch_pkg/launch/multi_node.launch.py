from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    # Turtle simulator node
    turtlesim = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim'
    )

    # Teleop node (keyboard control)
    teleop = Node(
        package='turtlesim',
        executable='turtle_teleop_key',
        name='teleop'
    )

    return LaunchDescription([
        turtlesim,
        teleop
    ])
