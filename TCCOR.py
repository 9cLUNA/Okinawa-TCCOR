from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import regex as re
import pytesseract as pt
from PIL import Image
import io
import os
from os import listdir
from os.path import isfile, join

# absolute path for file and directory
current_file_path = __file__
current_file_dir = os.path.dirname(__file__)

# get all possible tccor var, dirty
tccor_vars_file = os.path.join(current_file_dir, "tccor_variables.csv")
# get absolute values, clean
tccor_var_absolute = os.path.join(current_file_dir, "tccor_var_absolute.txt")
# get absolute path to original_img
original_img_dir = os.path.join(current_file_dir, "original_img")
# get absolute path to test_imgs
test_img_dir = os.path.join(current_file_dir, "test_imgs")

# get all test images into a list
img_files = [f for f in listdir(original_img_dir) if isfile(join(original_img_dir, f))]

# put possible tccor values into list
with open(tccor_vars_file) as f :
    tccor_list = [line.rstrip() for line in f]

# put absolute tccor values into list
with open(tccor_var_absolute) as tc :
    tccor_abs_value = [line.rstrip() for line in tc]

key = 0
for filenames in img_files :
    tccordata = ""
    testimg = os.path.join(current_file_dir,
                    'original_img',
                    img_files[key])
    resizetestimg = os.path.join(current_file_dir,
                    'test_imgs',
                    img_files[key])

    image = Image.open(testimg)
    # enlarge img for better accuracy
    basewidth = 4000
    wpercent = (basewidth/float(image.size[0]))
    hsize = int((float(image.size[1])*float(wpercent)))
    image = image.resize((basewidth,hsize), Image.ANTIALIAS)
    # ensure saving image with 300 dpi
    image.save(resizetestimg, dpi=(400,400))
    # pytesseract work
    #tccordata = pt.image_to_string(resizetestimg, config='--psm 11 --user-words tccor_var_absolute')
    tccordata = pt.image_to_string(resizetestimg, config='--psm 11')

    # match testing
    matches = next((x for x in tccor_abs_value if x in tccordata), False)

    print('Testing ' + img_files[key] + ". Tesseract matched: {}".format(matches))
    key += 1