# yolov7
# └── datasets
#     └── yourname
#         ├── images/
#         │   ├── train/  存放训练图片
#         │   └── val/    存放验证图片
#         ├── labels/
#         │   ├─ train/   存放训练标签  class x_center y_center width height
#         │   └── val/    存放验证标签
#         ├── train-list.txt
#         └── val-list.txt


import os
import sys
os.chdir(sys.path[0])


BASE_PATH = 'datasets'


def write(datadir):
    """生成训练验证图片路径

    Args:
        datadir (str): datasets内的文件夹名字,比如 coco128
    """
    image_dir = os.path.join(datadir, "images")         # class5/images/
    train_val = os.listdir(image_dir)                   # ['train', 'val']
    for t_v in train_val:
        in_image_dir = os.path.join(image_dir, t_v)     # class5/images/train
        images = os.listdir(in_image_dir)               # ['1.jpg', '2.jpg', '3.jpg'...]
        full_image_path = [os.path.join(BASE_PATH, in_image_dir, image) for image in images]   # datasets\class5\images\train\1.jpg

        with open(os.path.join(datadir, f"{t_v}-list.txt"), mode='w', encoding='utf-8') as f:
            for image_path in full_image_path:
                f.write(image_path+"\n")
        print(f"generating {len(images)} image path in {t_v}-list.txt!")


if __name__ == "__main__":
    write(datadir="class5")
