# ROS 2 Basic Definitions

## Node
A node is an executable process in ROS 2 that performs computation and communicates with other nodes.

## Topic
A topic is a named communication channel used by nodes to publish and subscribe to streaming data messages.

## Package
A package is the smallest organizational unit in ROS 2 that contains nodes, libraries, configuration files, and metadata.

## Workspace
A workspace is a directory structure where multiple ROS 2 packages are developed, built, and managed together.

##  Why is sourcing required? What happens if you do not source a workspace?
Sourcing sets up environment variables so the system can locate ROS 2 packages, executables, and dependencies in the workspace.  
If you do not source it, ROS 2 will not recognize your packages and commands like `ros2 run` will fail.

## What is the purpose of colcon build? What folders does it generate?
`colcon build` compiles and installs all packages inside a workspace.  
It generates three main folders: `build/`, `install/`, and `log/`.

## What does the entry_points console script do in setup.py?
The `entry_points` console script creates executable command-line tools for your ROS 2 nodes.  
It maps a terminal command to a specific Python function (usually `main()`).

## Publisher–Subscriber Diagram

A publisher sends messages to a topic, and a subscriber receives messages from that topic.  
The topic acts as the communication channel between them.

