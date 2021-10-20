from string import Template
import os
import linecache
from userFunctions import *

weeklyDirectory = "generated/notes/lessons-flat"
array = []
for filename in os.listdir(weeklyDirectory):
    weekly = open (weeklyDirectory+"/"+filename, "r")

    lines = weekly.readlines()

    # For Akanksha: Check this part for getting the specific includegraphics fragments
    for line in lines:
        if("\includegraphics" in line):
            x = (line[line.index("\includegraphics"):])
            x = (x[:x.index("}") + 1])
            x = x.replace("\n", "")
            x = x.replace(" ", "")
            array.append(x)
        
for i in array:
    print(i)