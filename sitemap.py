from string import Template
import os
from os import listdir
from os.path import isfile, join
import linecache
from user_functions import *

files = "generated/website"
arr = []
for entry in os.scandir(files):
    if entry.is_file():
        str = entry.name
        if("html" in str):
            # print("https://discrete-math-for-cs.github.io/website/" + entry.name)
            #TODO: make sure this can serve different URLs!! 
            arr.append("https://discrete-math-for-cs.github.io/website/" + entry.name)
# print(arr)

with open('generated/website/sitemap.txt', 'w') as f:
    for i in range(len(arr)):
        f.write(arr[i] + '\n')