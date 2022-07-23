from string import Template
import json
from user_functions import *
import collections
from string import Template
import os
from os import listdir
from os.path import isfile, join
import linecache

# Open JSON files
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
        # Key: Subtopic and count (i-th in the collapsible boxes)
        # Value: html
        key = small + str(count)
        html = outcomeData[big]['Children'][med]['file']
        outcome[key.lower()] = html
        count += 1


# Application
for key in applicationData:
    # Key: Application and # identifier
    # Value: html
    key = key.lower() + "#"
    html = key.replace(" ", "-").lower()+".html"
    outcome[key] = html

# print(outcome)

# Definition in activity-snippets --> go to the earliest week that the activity-snippet is used and the specific part
files = "notes/activity-snippets"
arr = []
newarr = []
for entry in os.scandir(files):
    if entry.is_file():
        # file: entry name and remove .tex
        file = entry.name[:-4]
        strName = file.replace("-", " ")

        # only get activity-snippets with definition in it
        if("definition" in strName):
            outcome[strName.lower()] = (file)


# Sort the elements
outcome = collections.OrderedDict(sorted(outcome.items()))

# Alphabetical view on top
content = ""

content += "<h1> "
alphabet = []

print(outcome)

for i in outcome:
    if(i[0] not in alphabet):
        alphabet.append(i[0])
        content += """<a href=\"glossary.html#""" + i[0] + """\">"""
        content += i[0]
        content += " </a>"
        content += " | "
content = content[:-2]
content += " </h1>\n"


# PART to get which activity snippets are included in each week
files = "notes/lessons"

# key is week and value is activity snippets
contents = {}

for entry in os.scandir(files):
    file = open(entry, 'r').readlines()
    if (len(file) > 0) and ("Week" in entry.name):
        week = entry.name.replace(".tex", "")
        dateIncluded = ""
        for line in file:
            # Get specific date which that activity-snippet was included
            if("\section*" in line):
                dateIncluded = line.replace("\section*{","").replace("}","")
            if ("\input" in line) and ("definition" in line) and ("lesson-head" not in line):
                cut = "{../activity-snippets/"
                line = line[line.index(cut) + len(cut):].replace("}", "").replace(".tex","").replace("\n", "").replace("-", " ")

                if(line not in contents):
                    contents[line] = []
                contents[line].append(week + " " + dateIncluded)

pdfCount = 0

# Each alphabet content
for j in alphabet:
    content += """<h1 id=\"""" + j + """\">""" + j + "</h1>\n"
    for key in outcome:
        # print(key)
        if (key[0] == j):
            # For learning outcome
            if (key[len(key) -1] in num):
                content += """<p>""" + key[:-1] + """  {<a href=\"""" + outcome[key] + """?box=""" + key[len(key) -1] + """\">Learning outcome</a>}</p>\n"""
            # For application
            elif(key[len(key) -1] == "#"):
                content += """<p>""" + key[:-1] + """   {<a href=\"""" + outcome[key].replace('#','')  + """\">Application</a>}</p>\n"""
                # print(outcome[key].replace('#',''))
            # For activity-snippets
            else:
                if(key in contents):
                    pdfCount += 1; 
                    whatWeek = str(contents[key][0])
                    if(("definition" in key) and ("definitions" != key)):
                        # print(key)
                        title = key.replace("definitions","").replace("definition","").strip()
                    else:
                        title = key
                    #print(key.replace(" ", "-"))
                    htmlPath = "../output/activity-snippets/"+key.replace(" ", "-")+".html"
                    content += """<p style="display: inline-block;">""" + title + """ {<a onclick="showDiv"""+str(pdfCount)+"""()" href="javascript:void(0)">Definition</a>"""
                    
                    #content += """<p>""" + title +"""{<a href=\"../output/activity-snippets/""" + key.replace(" ", "-")  + """.pdf\" download>Definition</a>}"""
                    content += """}{Week(s) included: """
                    for weeks in contents[key]:
                        numVal = weeks.index(" ")
                        numonly = weeks[:numVal][-1:]
                        # print(numonly)
                        content += """<a href=\"unit""" + numonly  + """.html#Notes\">""" + weeks + """&nbsp</a>"""
                        # print(weeks)
                        #<iframe class="PDFjs" src=\"web/viewer.html?file=../../output/activity-snippets/"""+ key.replace(" ", "-")+""".pdf\"title="webviewer" frameborder="0" width="70%" height="400"></iframe>
                    content += """}</p><br>
                    <div id="pdfDiv"""+str(pdfCount)+"""\"  style="display:none;"> 
                    <iframe class="glossaryPDFDiv" width="73%" height="300" src=\""""+htmlPath+ """\" title="description"></iframe>
                    
                    </div>
                    
                    <script>
                    function showDiv"""+str(pdfCount)+"""() {
                    var element = document.getElementById('pdfDiv"""+str(pdfCount)+"""'),
                    style = window.getComputedStyle(element);
                    if(style.getPropertyValue('display')=== 'none'){
                        document.getElementById("pdfDiv"""+str(pdfCount)+"""\").style.display = "block";
                    }
                    else{
                        document.getElementById("pdfDiv"""+str(pdfCount)+"""\").style.display = "none";
                    }
                    }
                    </script>
                    """
    content += "\n"

glossary_template = open("templates/glossary_template.html", "r")
templateString = Template(glossary_template.read())

page_variables = site_variables.copy()
page_variables.update(dict(
    content = content
))

#substitute settings unitData with appropriate variables 
result = templateString.substitute(page_variables)

write_if_different("generated/website/glossary.html", result)
        
glossary_template.close()