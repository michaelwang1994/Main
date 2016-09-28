import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import cm
%matplotlib inline

class img_data(imgpath):
    __init__(self):
        self.imgpath = imgpath
        self.data = self.img_bw_data(self.imgpath)
        self.fields = self.get_one_array(self.data, 50)



    def img_bw_data(self):
        # type: (object) -> object
        img = Image.open(self.imgpath)
        img_bw = img.convert('L')
        pixels_array = np.where(np.asarray(img_bw) > 255/2, 0, 1)
        return pixels_array

    def display(self):
        plt.figure(figsize = np.multiply(img.shape, 0.01))
        plt.axis('off')
        plt.imshow(img, cmap=cm.binary)

    def get_fields(imgpath):
        img_dict = {}
        imgname = 'Files' + imgpath.split('/')[-1]
        for index, row in data[data['ImagePath'] == imgname].iterrows():
            filepath = row['full_imgpath'].split('/')[-1]
            if not filepath in img_dict:
                img = img_bw_data(row['full_imgpath'])
                img_dict[filepath] = [img, np.zeros(img.shape)]
                x, y, x1, y1 = row['X'], row['Y'], row['X'] + row['W'], row['Y'] + row['H']
                img_dict[filepath][-1][y:y1, x:x1] = np.ones((y1 - y, x1 - x))
            else:
                x, y, x1, y1 = row['X'], row['Y'], row['X'] + row['W'], row['Y'] + row['H']
                img_dict[filepath][-1][y:y1, x:x1] = np.ones((y1 - y, x1 - x))
        return img_dict

    def get_one_groups(line, line_qualifier):
        pixel_index = 0
        pixel_final = 0
        one_groups = []
        for i, pixel in enumerate(line):
            if pixel == 1:
                if pixel_index:
                    pixel_final = i
                else:
                    pixel_index = i
            else:
                if pixel_final - line_qualifier > pixel_index:
                    one_groups.append((pixel_index, pixel_final))
                pixel_index = 0
                pixel_final = 0
        return one_groups

    def get_one_array(img, line_qualifier):
        one_array = np.zeros(img.shape)
        for i, line in enumerate(img):
            one_groups = get_one_groups(line, line_qualifier)
            for group in one_groups:
                one_array[i, group[0]:group[1]] = 1
        return one_array