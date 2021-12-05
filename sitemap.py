from string import Template
import os
from os import listdir
from os.path import isfile, join
import linecache
from user_functions import *

files = "generated/website"
websiteData = json.loads(open("website-settings.json").read())

# Iterate through generated/website folder
# Append all web pages to arr
arr = []
for entry in os.scandir(files):
    if entry.is_file():
        str = entry.name
        if("html" in str):
            arr.append(websiteData["Domain Name"] + entry.name)

# Write result to sitemap.txt
with open('generated/website/sitemap.txt', 'w') as f:
    for i in arr:
        f.write(i+ '\n')