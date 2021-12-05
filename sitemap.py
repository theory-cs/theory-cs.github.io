from string import Template
import os
from os import listdir
from os.path import isfile, join
import linecache
from user_functions import *

files = "generated/website"
websiteData = json.loads(open("website-settings.json").read())
arr = []
for entry in os.scandir(files):
    if entry.is_file():
        str = entry.name
        if("html" in str):
            arr.append(websiteData["Domain Name"] + entry.name)
# print(arr)

with open('generated/website/sitemap.txt', 'w') as f:
    for i in range(len(arr)):
        f.write(arr[i] + '\n')