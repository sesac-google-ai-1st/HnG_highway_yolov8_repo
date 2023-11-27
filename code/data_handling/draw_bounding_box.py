import glob
import os
import cv2
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.patches as patches


def glob_files(path, file_type="*"):
    search_string = os.path.join(path, file_type)
    files = glob.glob(search_string)

    # print('searching ', path)
    paths = []
    for f in files:
      if os.path.isdir(f):
        sub_paths = glob_files(f + '/')
        paths += sub_paths
      else:
        paths.append(f)

    # We sort the images in alphabetical order to match them
    #  to the annotation files
    paths.sort()

    return paths



show_n = 3   ### 3개만

def load_images(path):
    files = glob_files(path, "*.png")

    files.sort()

    # print(files)
    X_data = []
    for file in files[:show_n]:
        print(file)
        image = cv2.imread(file)
        # print(image.shape)
        # x = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

        X_data.append(image)
    return np.array(X_data)


# 이미지에 따라 크기 다를 수 있음
def get_w_h(img_list):
    width_list = []
    height_list = []
    for img in img_list:
        h, w, c = img.shape
        width_list.append(w)
        height_list.append(h)
    return width_list, height_list


WIDTH = 1080
HEIGHT = 1920

def load_labels(path):
    files = glob_files(path, "*.txt")
    files.sort()
    Y_data = []
    for i, file in enumerate(files[:show_n]):
        print(file)
        with open(file) as f:
            lines = f.readlines()

            boxes = []
            for line in lines:
                tokens = line.split()

                class_id = int(tokens[0])
                xc = float(tokens[1]) * WIDTH
                yc = float(tokens[2]) * HEIGHT
                width = float(tokens[3]) * WIDTH
                height = float(tokens[4]) * HEIGHT

                boxes.append(np.array([class_id, xc, yc, width, height]))
                # print(class_id, xc, yc, width, height)

            Y_data.append(np.array(boxes))
            # print(lines)
    return np.array(Y_data, dtype='object')





def create_patch_rectangle(y, color):
    # # in yolov5
    width = int(y[2])
    height = int(y[3])
    return patches.Rectangle((int(y[0] - width/2), int(y[1] - height/2)),
                            width, height,
                            edgecolor=color, fill=False)

COLORS = [(0, 255/255, 0), (255/255, 255/255, 0), (255/255, 0, 0)]

def plot_image(image, boxes, axis):
    # # print(boxes.shape)
    for box in boxes:
        # print(box)
        class_id = int(box[0])
        # print(type(class_id), class_id)
        rect = create_patch_rectangle(box[1:], COLORS[class_id])
        axis.add_patch(rect)

    plt.imshow(image)

def plot_images(X, Y, limit=10):
    fig = plt.figure(figsize=(100, 80))

    last_id = min(limit, X.shape[0])
    for id in range(last_id):
        axis = fig.add_subplot(5, 3, id + 1)
        axis.get_xaxis().set_visible(False)
        axis.get_yaxis().set_visible(False)
        plot_image(X[id], Y[id], axis)