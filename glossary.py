from string import Template
import json
from userFunctions import *
import collections
from string import Template
import os
from os import listdir
from os.path import isfile, join
import linecache

outcomeData = json.loads(open("outcomes.json").read())
applicationData = json.loads(open("applications.json").read())
num = "1234567890"


# Outcome
outcome = {}
count = 1
for big in outcomeData:
  for med in outcomeData[big]['Children']:
    count = 1
    for small in outcomeData[big]['Children'][med]['Children']:
        # print(small)
        # print(count)
        outcome[small + str(count)] = outcomeData[big]['Children'][med]['file']
        count += 1

# Application
for key in applicationData:
    print(key)
    html = key.replace(" ", "-").lower()+".html"
    print(html)
    outcome[key.lower()] = html

# Definition in activity-snippets --> go to the earliest week that the activity-snippet is used and the specific part
files = "notes/activity-snippets"
arr = []
newarr = []
for entry in os.scandir(files):
    if entry.is_file():
        file = entry.name[:-4]
        str = file.replace("-", " ")
        # print(str)
        if("definition" in str):
            outcome[str] = (file)

outcome = collections.OrderedDict(sorted(outcome.items()))
# print(outcome)



# Alphabetical view on top
content = ""
content += "<h1> "
alphabet = []
for i in outcome:
    # print(i)
    if(i[0] not in alphabet):
        alphabet.append(i[0])
        content += """<a href=\"glossary.html#""" + i[0] + """\">"""
        content += i[0]
        content += " </a>"
        content += " | "
content = content[:-2]
content += " </h1>\n"


# Each alphabet content
for j in alphabet:
    content += """<h1 id=\"""" + j + """\">""" + j + "</h1>\n"
    # print(j)
    for key in outcome:
        # print(key)
        if(key[0] == j):
            if(key[len(key) -1] in num):
                content += """<p><a href=\"""" + outcome[key]  + """?box=""" + key[len(key) -1] + """\">""" + key[:-1] +"""</a></p>\n"""
            else:
                content += """<p><a href=\"""" + outcome[key]  + """\">""" + key +"""</a></p>\n"""
                # content += """<p><a href=\"../notes/activity-snippets/""" + outcome[key]  + """\">""" + key +"""</a></p>\n"""
    content += "\n"

# print(content)

glossaryTemplate = open("templates/glossaryTemplate.html", "r")
templateString = Template(glossaryTemplate.read())

page_variables = site_variables.copy()
page_variables.update(dict(
    content = content
))

#substitute settings unitData with appropriate variables 
result = templateString.substitute(page_variables)


resultFile = open("generated/website/glossary.html", "w")
resultFile.write(result)
resultFile.close()
        
glossaryTemplate.close()

