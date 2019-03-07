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
# get absolute values, clean
tccor_var_absolute = os.path.join(current_file_dir, "tccor_var_absolute.txt")
# get absolute path for tmp img file
tmp_img = os.path.join(current_file_dir, "tmp_img.jpg")

url = 'http://www.kadena.af.mil/Agencies/Local-Weather'

# Need to find way to actively find this div even if number changes...

soup = BeautifulSoup(urlopen(url).read(), "html.parser")
tccor = soup.find("div", {"id": "dnn_ctr26874_HtmlModule_lblContent"})

print(tccor)