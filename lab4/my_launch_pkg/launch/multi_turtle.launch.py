from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():

    # First turtle simulator
    turtlesim_node = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim'
    )

    # Spawn second turtle
    spawn_turtle = ExecuteProcess(
        cmd=[
            'ros2', 'service', 'call',
            '/spawn', 'turtlesim/srv/Spawn',
            '{x: 2.0, y: 2.0, theta: 0.0, name: "turtle2"}'
        ],
        output='screen'
    )

    return LaunchDescription([
        turtlesim_node,
        spawn_turtle
    ])
