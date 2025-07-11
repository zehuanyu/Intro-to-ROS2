# Intro to ROS2

This repository contains a simple ROS2 package demonstrating the fundamental concepts of ROS2, including nodes, topics, publishers, subscribers, and launch files.

---

## Overview

The project implements basic ROS2 nodes that communicate via topics. It includes:

- A publisher node that sends messages periodically  
- A subscriber node that receives and processes those messages  
- A launch file to start the nodes together  

This serves as a practical introduction to ROS2 programming and workflows.

---

## Prerequisites

- Ubuntu 20.04 or later (tested on Ubuntu 20.04)  
- ROS2 Foxy Fitzroy installed ([ROS2 installation guide](https://docs.ros.org/en/foxy/Installation.html))  
- Python 3.8+  

---

## Setup Instructions

### :one: Clone the repository

```bash
git clone https://github.com/zehuanyu/Intro-to-ROS2.git
cd Intro-to-ROS2
```

### :two: Source your ROS2 environment

```bash
source /opt/ros/foxy/setup.bash
```

### :three: Build the workspace

```bash
colcon build --symlink-install
```
### :four: Source the workspace overlay

```bash
source install/setup.bash
```
## Running the Nodes

Launch the publisher and subscriber nodes with:

```bash
ros2 launch lab1_pkg lab1_launch.py
```

You should see messages published and received in the terminal output.

## Code Structure
- src/lab1_pkg/lab1_pkg/: ROS2 package source code
- src/lab1_pkg/lab1_pkg/lab1_launch.py: Launch file to start nodes
- setup.py, package.xml: ROS2 package build files


