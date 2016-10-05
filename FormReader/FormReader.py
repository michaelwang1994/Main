import cv2
import numpy as np
import pandas as pd
from PIL import Image
import pytesseract as pyt
import sys
import datetime

class Image_Data:

    def __init__(self, imgpath):
        self.img_pil = Image.open(imgpath)
        self.img_pil_gray = self.img_pil.convert('L')
        self.img = cv2.imread(imgpath)

        self.height, self.width, self.channels = self.img.shape
        pyt_string = pyt.image_to_string(self.img_pil_gray, boxes=True)
        pyt_string_split = pyt_string.split('\n')
        self.string_split = [split.split() for split in pyt_string_split]
        self.char_array, self.special_char_array = self.get_char_arrays()
        self.wordless_img = cv2.drawContours(self.img, self.char_array, -1, (255, 255, 255), -1)
        self.wordless_img = cv2.drawContours(self.wordless_img, self.char_array, -1, (255, 255, 255), 2)
        self.imgray = cv2.cvtColor(self.wordless_img, cv2.COLOR_BGR2GRAY)

        ret, thresh = cv2.threshold(self.imgray, 127, 255, 0)
        self.image, self.contours, self.hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cont_hierarchy = np.array(zip(self.contours, self.hierarchy[0][:, 2]))
        self.real_contours = cont_hierarchy[cont_hierarchy[:, 1] == -1][:, 0]
        self.real_contours = self.get_array_size()
        self.final_img = cv2.drawContours(cv2.imread(imgpath), self.real_contours, -1, (0, 255, 0), 2)
        self.final_img = cv2.drawContours(self.final_img, self.special_char_array, -1, (0, 255, 0), 2)

    def get_wordless_img(self):
        cv2.imwrite('wordless_' + sys.argv[1], self.wordless_img)

    def get_final_img(self):
        cv2.imwrite('final_' + sys.argv[1], self.final_img)

    def get_img_string(self):
        print pyt.image_to_string(self.img_pil_gray)

    def get_char_arrays(self):
        char_list = []
        special_char_list = []
        for char_split in self.string_split:
            char_id = char_split[0]

            char_split_s = self.height - int(char_split[2])
            char_split_w = int(char_split[1])
            char_split_n = self.height - int(char_split[4])
            char_split_e = int(char_split[3])

            char_boundaries = np.array([[[char_split_e, char_split_s]], [[char_split_e, char_split_n]],
                                        [[char_split_w, char_split_n]], [[char_split_w, char_split_s]]])

            if (char_id != '~') & (char_id != '_') & (char_id != ':') & (char_id != '?'):
                char_list.append(char_boundaries)
            elif (char_id == ':') | (char_id == '?'):
                special_char_list.append(char_boundaries)

        return char_list, special_char_list

    def get_array_size(self):
        contours_to_keep = []
        for i, contour in enumerate(self.real_contours):
            x = contour[:, 0, 0]
            y = contour[:, 0, 1]
            min_x, max_x = np.min(x), np.max(x)
            min_y, max_y = np.min(y), np.max(y)
            area = (max_x - min_x)*(max_y - min_y)
            if area > 50:
                contours_to_keep.append(i)

        return self.real_contours[contours_to_keep]
print 'start time %s' % (datetime.datetime.now())
imgpath = str(sys.argv[1])
test = Image_Data(imgpath)

print 'end time %s' % (datetime.datetime.now())
test.get_final_img()
