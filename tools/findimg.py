import glob
import os
import cv2 as cv
def get_cover(input_dir, color_format="ppm", depth_format="pgm"):
    # 准备数据
    if not os.path.exists(input_dir):
        print("[ERROR] 路径不存在")
        exit(-1)
    color_paths = sorted(glob.glob(os.path.join(input_dir, "*" + color_format)))
    depth_paths = sorted(glob.glob(os.path.join(input_dir, "*" + depth_format)))
    if len(color_paths) != len(depth_paths):
        print("[ERROR] 深度图和彩色图数量不匹配！")
        exit(-1)
    if len(color_paths) == 0 or len(depth_paths) == 0:
        print("[ERROR] 路径下没有图片")
        exit(-1)
    # 计算权重
    weight = [None] * len(color_paths)
    for i, (color_path, depth_path) in enumerate(zip(*[color_paths, depth_paths])):
        color_img = cv.imread(color_path, cv.IMREAD_UNCHANGED)
        depth_img = cv.imread(depth_path, cv.IMREAD_UNCHANGED)
        edge = cv.Canny(color_img, 0, 100)          # 手动调参
        weight[i] = edge.sum() * depth_img.mean()   # edge丰富、平均距离大的图片，权重更高
    max_idx = weight.index(max(weight))
    return color_paths[max_idx]
if __name__ == '__main__':
    input_dir = "/origin_data/scene2_origin"

    print(get_cover(input_dir))