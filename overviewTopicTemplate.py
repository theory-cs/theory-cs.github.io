from string import Template
import json
  
# Opening JSON file
fileJson = open('outcomeTest.json',)
  
# returns JSON object as a dictionary
data = json.load(fileJson)

sidebarButtons = ""
for i in data:
    for j in data[i]['Children']:
        #only put icon in sidebar of 2nd tier topics that have children 
        if(bool(data[i]['Children'][j]['Children'])):
            sidebarButtons += "<li>"
            sidebarButtons += """<a href= \"""" +data[i]['Children'][j]['file'] + """\" aria-label="Go to """ + j + """ ">"""
            sidebarButtons += """<i><p class="icons">&nbsp;&nbsp;""" + data[i]['Children'][j]['Icon'] + """</p></i>"""
            sidebarButtons += """<span class="links_name"> """ + j + """</span>"""
            sidebarButtons += "</a>"
            sidebarButtons += """<span class="tooltip"> """ + j + """</span>"""
            sidebarButtons += "</li>"

mobileSidebar = ""
for i in data:
    for j in data[i]['Children']:
        #only put icon in sidebar of 2nd tier topics that have children 
        if(bool(data[i]['Children'][j]['Children'])):
            mobileSidebar += """<a href= \"""" + data[i]['Children'][j]['file'] + """\"">""" + j + """</a>"""



boxString = ""
#big for loop begin
for i in data:

    boxString += """<div class="box">"""

    boxString += "<h2>" + data[i]['Icon'] + i + "</h2>"
    boxString += "<p> Program Level: " + data[i]['Program Level'] + "</p>"
    boxString += "<p> Theory: " + data[i]['Theory'] + "</p>"
    boxString += "<hr>"

    boxString += """<div class="column">"""

    
    for j in data[i]['Children']:

        if(bool(data[i]['Children'][j]['Children'])):
             boxString += """<h3 style="font-size: 20px;"><a href=\"""" + data[i]['Children'][j]['file'] + """\" style=" color: black;">""" + j + """</a></h3>"""
             
        else:
            boxString += """<h3 style="font-size: 20px;"><a href="javascript:void(0)" style=" color: black;">""" + j + """</a></h3>"""
           

        if(bool(data[i]['Children'][j]['Children'])):
            boxString += """<ul style="font-size: 13px;">"""
            for k in data[i]['Children'][j]['Children']:
                boxString += "<li>" + k + "</li>"
            
            boxString += "</ul>"

    boxString += "</div>"

    boxString += "</div>"
    
#open unitTemplate html file and read it into a string 
unitTemplate = open("overviewTopicTemplate.html", "r")
templateString = Template(unitTemplate.read())

#substitute settings data with appropriate variables 
result = templateString.safe_substitute(
    sidebar = sidebarButtons,
    mobile = mobileSidebar,
    boxes = boxString
)


resultFile = open("generated/website/overviewTopicTemplate.html", "w")
resultFile.write(result)
resultFile.close()



# Closing files
fileJson.close()
