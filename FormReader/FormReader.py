import cv2
import numpy as np
from PIL import Image
import pytesseract as pyt
import sys
from imutils.perspective import four_point_transform
from skimage.filters import threshold_adaptive

class Image_Data:

    def __init__(self, imgpath, is_camera=False):

        if is_camera:
            self.img = cv2.imread(imgpath)
            self.img = cv2.resize(self.img.copy(), (int(.95*self.img.shape[1]), int(.95*self.img.shape[0])), interpolation = cv2.INTER_CUBIC)
            self.imggray_original = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            # cv2.imshow("test", self.img.copy())
            # cv2.waitKey(0)

            gray = cv2.GaussianBlur(self.imggray_original, (5, 5), 0)
            edged = cv2.Canny(gray, 75, 200)
            # cv2.imshow("test", gray)
            cv2.imshow("test", cv2.resize(edged.copy(), (int(.5*self.img.shape[1]), int(.5*self.img.shape[0])), interpolation = cv2.INTER_CUBIC))
            cv2.waitKey(0)

            img, contours, heir = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=cv2.contourArea, reverse=True)

            # loop over the contours
            for i, contour in enumerate(contours):
                # approximate the contour
                peri = cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, 0.05 * peri, True)

                # if our approximated contour has four points, then we
                # can assume that we have found our screen
                if len(approx) == 4:
                # if i == 0:
                    screenCnt = approx
                    # cv2.imshow("test", cv2.drawContours(self.img.copy(), contour, -1, (255, 0, 0), 2))
                    self.img = four_point_transform(self.img.copy(), screenCnt.reshape(4, 2))
                    self.imggray_original = four_point_transform(gray, screenCnt.reshape(4, 2))
                    self.imggray_original = threshold_adaptive(self.imggray_original, 251, offset=10)
                    self.imggray_original = self.imggray_original.astype("uint8") * 255

                    self.height, self.width, self.channels = self.img.shape
                    cv2.imshow("test", cv2.resize(self.imggray_original, (int(.5 * self.img.shape[1]), int(.5 * self.img.shape[0])), interpolation=cv2.INTER_CUBIC))
                    cv2.waitKey(0)
                    self.img_pil_gray = Image.fromarray(self.imggray_original)
                    self.imgpath = imgpath
                    self.window_height = int(.01 * self.height)
                    self.window_width = int(.01 * self.width)

                    break

        else:
            self.img = cv2.imread(imgpath)
            self.imggray_original = cv2.cvtColor(self.img.copy(), cv2.COLOR_BGR2GRAY)

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
        self.wordless_img = cv2.drawContours(self.img.copy(), self.char_array, -1, (255, 255, 255), -1)
        self.wordless_img = cv2.drawContours(self.wordless_img, self.char_array, -1, (255, 255, 255), 2)
        self.imgray = cv2.cvtColor(self.wordless_img, cv2.COLOR_BGR2GRAY)

    def extract_contours(self):
        ret, thresh = cv2.threshold(self.imgray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        # thresh = cv2.adaptiveThreshold(self.imgray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        self.image, self.contours, self.hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.real_contours = np.array(self.contours)[self.hierarchy[0][:, 2] == -1]
        self.real_contours = self.add_special_contours()
        self.real_contours = self.get_array_size()

    def add_contours(self):

        self.final_img = cv2.drawContours(self.img.copy(), self.special_char_array, -1, (0, 0, 255), 2)
        self.final_img = cv2.drawContours(self.final_img, self.char_array, -1, (255, 0, 0), 2)
        self.final_img = cv2.drawContours(self.final_img, self.real_contours, -1, (0, 255, 0), 2)
        # self.final_img = cv2.drawContours(self.final_img, self.special_contours, -1, (0, 0, 255), 2)

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

            try:
                new_contour, sample = self.resize_contour(contour)
                ret, sample_thresh = cv2.threshold(sample, 127, 255, cv2.THRESH_BINARY)
                sample_image, sample_contours, sample_hierarchy = cv2.findContours(sample_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                if len(sample_contours) < 2:
                    contours_to_keep.append(new_contour)
            except:
                next

        return np.array(np.array(contours_to_keep))

    def add_special_contours(self):
        special_contour_list = list(self.real_contours)
        for special_char in self.special_char_array:
            e = special_char[:, 0, 0][0]
            w = special_char[:, 0, 0][2]
            s = special_char[:, 0, 1][0]
            n = special_char[:, 0, 1][2]
            new_w = e + self.window_width
            new_n = int(n - .25 * self.window_height)
            new_s = int(s + .25 * self.window_height)
            sample = self.imggray_original[:, new_w:]
            color_test = sample[s, 0]
            try:
                e_test = (np.where(sample[new_n:new_s, :] != color_test)[1])
                if len(e_test) == 0:
                    new_e = self.width - self.window_width
                else:
                    new_e = np.min(e_test) + new_w - 5
                special_char_boundaries = np.array([[[new_e, new_s]], [[new_e, new_n]],
                                                    [[new_w, new_n]], [[new_w, new_s]]])
                special_contour_list.append(special_char_boundaries)
            except:
                next

        return np.array(special_contour_list)

    def resize_contour(self, contour):
        x = contour[:, 0, 0]
        y = contour[:, 0, 1]

        min_x, max_x = np.min(x), np.max(x)
        min_y, max_y = np.min(y), np.max(y)

        # expand contour if too small. turns contours into squares
        if np.abs(min_y - max_y) < self.window_height:
            new_contour = np.array([[[max_x, max_y]], [[max_x, max_y - self.window_height]],
                                    [[min_x, max_y - self.window_height]], [[min_x, max_y]]])
        else:
            new_contour = np.array([[[max_x, max_y]], [[max_x, min_y]],
                                    [[min_x, min_y]], [[min_x, max_y]]])

        new_x = new_contour[:, 0, 0]
        new_y = new_contour[:, 0, 1]

        min_x, max_x = np.min(new_x), np.max(new_x)
        min_y, max_y = np.min(new_y), np.max(new_y)

        area = (max_x - min_x) * (max_y - min_y)

        sample = self.imggray_original[min_y + 3:max_y - 3, min_x + 3:max_x - 3]

        # check if there are characters in contour
        char_conditions = (min_x < self.x_vals_w) & (max_x > self.x_vals_e) & (min_y < self.y_vals_s) & (max_y > self.y_vals_n)
        contains_chars = np.array(self.char_list)[char_conditions]

        # check if the contour is big enough
        area_condition_mult = (area > 2 * self.window_height * self.window_width)
        area_condition_size = (max_x - min_x > self.window_width)

        if (area_condition_mult) & (area_condition_size):
            if max_x - min_x > max_y - min_y:
                if len(contains_chars) == 0:
                    print np.unique(sample)
                    return new_contour, sample
                    # if len(np.unique(sample)) <= 3:
