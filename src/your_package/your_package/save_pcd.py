import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from sensor_msgs_py import point_cloud2
import numpy as np
import open3d as o3d


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
        pc_arr = point_cloud2.read_points(
            msg, field_names=("x", "y", "z"), skip_nans=True)
        points = np.array(list(pc_arr))

        # save to PCD at a certain instance
        if self.pcd_counter < 10:  # adjust this condition as needed
            pcd = o3d.geometry.PointCloud()
            pcd.points = o3d.utility.Vector3dVector(points.astype(np.float32))
            o3d.io.write_point_cloud(f"cloud{self.pcd_counter}.pcd", pcd)
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
