from FormReader import Image_Data
import datetime
import sys

print 'start time %s' % (datetime.datetime.now())
imgpath = str(sys.argv[1])
test = Image_Data(imgpath)
test.extract_chars()
test.remove_chars()
test.extract_contours()
# test.text_from_contours()
test.add_contours()
test.get_final_img()
print 'end time %s' % (datetime.datetime.now())

