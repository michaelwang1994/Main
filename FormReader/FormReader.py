import cv2
import numpy as np
from PIL import Image
import pytesseract as pyt
import sys

class Image_Data:

    def __init__(self, imgpath):
        # TODO: Make image skew detector

        self.img = cv2.imread(imgpath)
        self.imggray_original = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.img_pil_gray = Image.fromarray(self.imggray_original)
        self.imgpath = imgpath
        self.height, self.width, self.channels = self.img.shape
        self.window_height = int(.01 * self.height)
        self.window_width = int(.01 * self.width)

    def extract_chars(self):
        pyt_string = pyt.image_to_string(self.img_pil_gray, boxes=True)
        pyt_string_split = pyt_string.split('\n')
        self.string_split = [split.split() for split in pyt_string_split]
        self.char_list, self.char_array, self.special_char_list, self.special_char_array = self.get_char_arrays()

    def remove_chars(self):
        self.wordless_img = cv2.drawContours(self.img, self.char_array, -1, (255, 255, 255), -1)
        self.wordless_img = cv2.drawContours(self.wordless_img, self.char_array, -1, (255, 255, 255), 2)
        self.imgray = cv2.cvtColor(self.wordless_img, cv2.COLOR_BGR2GRAY)

    def extract_contours(self):
        # ret, thresh = cv2.threshold(self.imgray, 127, 255, 0)
        thresh = cv2.adaptiveThreshold(self.imgray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        self.image, self.contours, self.hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.real_contours = np.array(self.contours)[self.hierarchy[0][:, 2] == -1]
        self.special_contours = self.add_special_contours()
        self.real_contours = self.get_array_size()

    def add_circles_and_squares(self):
        pass
        # TODO: add circles and squares

    def add_contours(self):

        self.final_img = cv2.drawContours(cv2.imread(self.imgpath), self.special_char_array, -1, (0, 0, 255), 2)
        self.final_img = cv2.drawContours(self.final_img, self.char_array, -1, (255, 0, 0), 2)
        self.final_img = cv2.drawContours(self.final_img, self.real_contours, -1, (0, 255, 0), 2)
        self.final_img = cv2.drawContours(self.final_img, self.special_contours, -1, (0, 0, 255), 2)

    def get_wordless_img(self):
        cv2.imwrite('wordless_' + sys.argv[1], self.wordless_img)

    def get_final_img(self):
        cv2.imwrite('final_' + sys.argv[1], self.final_img)

    def get_img_string(self):
        print pyt.image_to_string(self.img_pil_gray)

    def get_char_arrays(self):

        char_list = []
        char_area_list = []
        special_char_list = []
        special_char_area_list = []
        for char_split in self.string_split:
            char_id = char_split[0]

            char_split_s = self.height - int(char_split[2])
            char_split_w = int(char_split[1])
            char_split_n = self.height - int(char_split[4])
            char_split_e = int(char_split[3])

            char_boundaries = np.array([[[char_split_e, char_split_s]], [[char_split_e, char_split_n]],
                                        [[char_split_w, char_split_n]], [[char_split_w, char_split_s]]])

            if (char_id != '~') & (char_id != '_') & (char_id != '-') & (char_id != ':') & (char_id != '?'):
                char_list.append(char_id)
                char_area_list.append(char_boundaries)
            elif (char_id == ':') | (char_id == '?'):
                special_char_list.append(char_id)
                special_char_area_list.append(char_boundaries)

        char_array = np.array(char_area_list)
        self.x_vals_e = char_array[:, :, 0, 0][:, 0]
        self.x_vals_w = char_array[:, :, 0, 0][:, 2]

        self.y_vals_s = char_array[:, :, 0, 1][:, 0]
        self.y_vals_n = char_array[:, :, 0, 1][:, 2]
        return char_list, char_area_list, special_char_list, special_char_area_list

    def get_array_size(self):
        contours_to_keep = []
        for i, contour in enumerate(self.real_contours):
            x = contour[:, 0, 0]
            y = contour[:, 0, 1]

            min_x, max_x = np.min(x), np.max(x)
            min_y, max_y = np.min(y), np.max(y)
            area = (max_x - min_x)*(max_y - min_y)
            sample = self.imggray_original[min_y:max_y, min_x:max_x]

            contains_chars = np.array(self.char_list)[(min_x < self.x_vals_w) & (max_x > self.x_vals_e) &
                                                      (min_y < self.y_vals_s) & (max_y > self.y_vals_n)]
            if (area > self.window_height*self.window_width) or (np.abs(min_y - max_y) < self.window_height and np.abs(min_x - max_x) > self.window_width):
                if max_x - min_x > max_y - min_y:
                    try:
                        if len(contains_chars) == 0:
                            ret, sample_thresh = cv2.threshold(sample, 127, 255, cv2.THRESH_BINARY)
                            sample_image, sample_contours, sample_hierarchy = cv2.findContours(sample_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                            if len(sample_contours) < 3:
                                contours_to_keep.append(i)

                    except:
                        next
        return self.real_contours[contours_to_keep]

    def add_special_contours(self):
        # real_contour_list = list(self.real_contours)
        test_contour_list = []
        for special_char in self.special_char_array:
            e = special_char[:, 0, 0][0]
            w = special_char[:, 0, 0][2]
            s = special_char[:, 0, 1][0]
            n = special_char[:, 0, 1][2]
            # print "East: %s, West: %s, South: %s, North: %s" % (e, w, s, n)
            sample = self.imggray_original[e + self.window_width:, :]
            ret, sample_thresh = cv2.threshold(sample, 127, 255, cv2.THRESH_BINARY)
            sample_image, sample_contours, sample_hierarchy = cv2.findContours(sample_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            new_n = new_w = 0
            new_s = self.height
            new_e = self.width

            for contour in sample_contours:
                x = contour[:, 0, 0]
                y = contour[:, 0, 1]

                min_x, max_x = np.min(x), np.max(x)
                min_y, max_y = np.min(y), np.max(y)

                if min_y < s & min_y > new_s:
                    new_s = min_y
                if max_y > n & max_y > new_n:
                    new_n = max_y
                if min_x < w & min_x > new_w:
                    new_w = min_x
                if max_x > e & max_x < new_e:
                    new_e = max_x


            new_e = new_e + e + self.window_width
            new_w = e + self.window_width
            # print "East: %s, West: %s, South: %s, North: %s -- UPDATED" % (new_e, new_w, new_s, new_n)
            special_char_boundaries = np.array([[[new_e, new_s]], [[new_e, new_n]],
                                                [[new_w, new_n]], [[new_w, new_s]]])

            test_contour_list.append(special_char_boundaries)
        return np.array(test_contour_list)
