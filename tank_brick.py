import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

def plot(pcd):
    o3d.visualization.draw_geometries([pcd])
def display_inlier_outlier(cloud,ind):
    inlier_cloud = cloud.select_by_index(ind)
    outlier_cloud = cloud.select_by_index(ind,invert = True)



def main():
    pcd = o3d.io.read_point_cloud("converted_3D_data.ply")
    plot(pcd)
    voxel_down_pcd = pcd.voxel_down_sample(voxel_size = 10)
    plot(voxel_down_pcd)
    uni_down_pcd = pcd.uniform_down_samploe(every_k_point = 20)
    plot(uni_down_pcd)

if __name__ == '__main__':
    main()
