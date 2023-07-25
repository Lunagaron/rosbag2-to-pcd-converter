# PointCloud Saver ROS2 Package

This package provides a simple ROS2 node to capture PointCloud data from a topic and save the point cloud data as multiple PCD files.

## Dependencies

- ROS2 Galactic or above
- Python 3.7 or above
- Open3D
- Numpy

Make sure you have already installed ROS2 and setup your environment properly.

### Python Dependencies

You can install the python dependencies via pip:

```bash
pip install open3d numpy

```

## How to Use

1. Clone this package into your ROS2 workspace. For instance:

```bash
cd ~/ros2_ws/src
git clone <this repository>
```

2. Build your workspace:

```bash
cd ~/ros2_ws
colcon build --packages-select your_package
```

3. Source your workspace:

```bash
source ~/ros2_ws/install/setup.bash
```

4. Run the node:

```bash
ros2 run your_package save_pcd
```

Currently, this package will create PCD files in the current directory where you run the node. The node listens to the `/velodyne_points` topic and saves the first 10 point cloud messages it receives as PCD files named `cloud0.pcd`, `cloud1.pcd`, `cloud2.pcd`, and so forth.

## Configuration

To adjust the number of point cloud instances saved, you can modify the `if self.pcd_counter < 10:` line in `listener_callback` method within `save_pcd.py` script.

If your point cloud data is published on a different topic, modify the `'/velodyne_points'` argument in `create_subscription` method call within `__init__` function of the `SavePCDNode` class.
