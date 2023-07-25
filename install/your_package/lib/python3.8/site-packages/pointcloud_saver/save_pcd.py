import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
import numpy as np
import pcl

class SavePCDNode(Node):
    def __init__(self):
        super().__init__('save_pcd_node')
        self.subscription = self.create_subscription(
            PointCloud2,
            '/velodyne_points',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.pcd_counter = 0  # Counter for PCD files

    def listener_callback(self, msg):
        # convert the ROS PointCloud2 message to a 3D numpy array 
        pc_arr = pc2.read_points(msg, field_names=("x", "y", "z"), skip_nans=True)
        points = np.array(list(pc_arr))

        # save to PCD at a certain instance
        if self.pcd_counter < 10:  # adjust this condition as needed
            pcl.save(pcl.PointCloud(points.astype(np.float32)), f"cloud{self.pcd_counter}.pcd")
            self.pcd_counter += 1

def main(args=None):
    rclpy.init(args=args)

    node = SavePCDNode()

    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - done automatically when the script exits)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
