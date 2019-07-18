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
import shutil

# absolute path for file and directory
current_file_path = __file__
current_file_dir = os.path.dirname(__file__)

# get all possible tccor var, dirty
tccor_vars_file = os.path.join(current_file_dir, "tccor_variables.csv")

# get absolute values, cleanclear
tccor_var_absolute = os.path.join(current_file_dir, "tccor_var_absolute.txt")

# get absolute path for tmp img file
tmp_img = os.path.join(current_file_dir, "tmp_img.jpg")

url = 'http://www.kadena.af.mil/Agencies/Local-Weather'

# Need to find way to actively find this div even if number changes...
# perhaps use title bar "TYPHOON INFORMATION" instead
# and pull all info under it, if there is no image found, then search text
# for NO ACTIVE TCCOR
# and report that instead

soup = BeautifulSoup(urlopen(url).read(), "html.parser")

# Find the title text then find the img tag right after it
tccor = soup.find(text="Current TCCOR Information").findNext('img')['src']

urllink = 'https://www.kadena.af.mil' # first part of URL
tccorurl = urllink + tccor # create the complete url

tccorimg = requests.get(tccorurl, stream=True)
with open(tmp_img, 'wb') as out_file:
    shutil.copyfileobj(tccorimg.raw, out_file)

image = Image.open(tmp_img).convert('RGB')
# image might be gif and JPG doesn't support transparency
#image = image.convert('RGB')

# enlarge img for better accuracy
basewidth = 4000
wpercent = (basewidth/float(image.size[0]))
hsize = int((float(image.size[1])*float(wpercent)))
image = image.resize((basewidth,hsize), Image.ANTIALIAS)
# ensure saving image with 300 dpi
image.save(tmp_img, dpi=(400,400))
# pytesseract work
tccordata = pt.image_to_string(tmp_img, config='--psm 11')

# put possible tccor values into list
with open(tccor_vars_file) as f :
    tccor_list = [line.rstrip() for line in f]

# put absolute tccor values into list
with open(tccor_var_absolute) as tc :
    tccor_abs_value = [line.rstrip() for line in tc]

matches = next((x for x in tccor_abs_value if x in tccordata), False)
print("Tesseract matched: {}".format(matches))