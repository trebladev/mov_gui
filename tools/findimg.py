import glob
import os
import cv2 as cv


def get_cover(input_dir, color_format="ppm", depth_format="pgm"):
    # 准备数据：RGBD图片
    if not os.path.exists(input_dir):
        print("[ERROR] 路径不存在")
        exit(-1)
    color_paths = glob.glob(os.path.join(input_dir, "*" + color_format))
    depth_paths = glob.glob(os.path.join(input_dir, "*" + depth_format))
    color_paths.sort(key=lambda x: int(x.split("/")[-1].split(".")[0]))  # 按照文件中数字大小排序
    depth_paths.sort(key=lambda x: int(x.split("/")[-1].split(".")[0]))
    if len(color_paths) != len(depth_paths):
        print("[ERROR] 深度图和彩色图数量不匹配！")
        exit(-1)
    if len(color_paths) == 0 or len(depth_paths) == 0:
        print("[ERROR] 路径下没有图片")
        exit(-1)
    # 读取全部的camera pose
    with open(os.path.join(input_dir, "trajectory.txt"), "r") as f:
        camera_poses = f.readlines()
    # 计算权重
    weight = [None] * len(color_paths)
    for i, (color_path, depth_path) in enumerate(zip(*[color_paths, depth_paths])):
        color_img = cv.imread(color_path, cv.IMREAD_UNCHANGED)
        depth_img = cv.imread(depth_path, cv.IMREAD_UNCHANGED)
        edge = cv.Canny(color_img, 0, 100)  # 手动调参
        weight[i] = edge.sum() * depth_img.mean()  # edge丰富、平均距离大的图片，权重更高
    # 得到最大权重的id
    max_idx = weight.index(max(weight))
    # 记录对应的camera pose到txt中
    with open(os.path.join(input_dir, "camera_pose.txt"), "w") as f:
        f.write(camera_poses[max_idx])

    return color_paths[max_idx]


if __name__ == '__main__':
    input_dir = "/home/orz/Projects/FastFusion_obec_show/data/test1"

    print(get_cover(input_dir))
