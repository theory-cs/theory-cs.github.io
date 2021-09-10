from string import Template
import json
  
# Opening JSON file
fileJson = open('applications.json',)
  
# returns JSON object as a dictionary
data = json.load(fileJson)

#Adds icons in regular sidebar for each 2nd tier child in outcomes.json 
sidebarButtons = ""
for i in data:
    sidebarButtons += "<li>"
    sidebarButtons += """<a href= \"""" +data[i]['file'] + """\" aria-label="Go to """ + i + """">"""
    sidebarButtons += """<i><p class="icons">&nbsp;&nbsp;""" + data[i]['Icon'] + """</p></i>"""
    sidebarButtons += """<span class="links_name"> """ + i + """</span>"""
    sidebarButtons += "</a>"
    sidebarButtons += """<span class="tooltip"> """ + i + """</span>"""
    sidebarButtons += "</li>\n"

        
            

#Adds icons in regular sidebar for each 2nd tier child in outcomes.json 
mobileSidebar = ""
for i in data:
    mobileSidebar += """<a href= \"""" + data[i]['file'] + """">""" + i + """</a>"""

boxString = ""
#big for loop begin
for i in data:

    boxString += """<div class="box"> \n"""

    boxString += """<h2><a href= \"""" + data[i]['file'] + """\" style="color: #182B49; text-decoration: none;" >""" + i + """</a></h2>"""
    boxString += "<hr>"

    boxString += """<div class="column"> <dl> \n"""

    
    for j in data[i]['Children']:
        boxString += """<dt><a style="color: #00629B;"><i class='bx bx-subdirectory-right'></i>""" + j + """</a></dt> \n"""


            
    boxString += "</dl>"

    boxString += "</div>"

    boxString += "</div><br><br>"
    
#open unitTemplate html file and read it into a string 
unitTemplate = open("overviewApplicationTemplate.html", "r")
templateString = Template(unitTemplate.read())

#substitute settings data with appropriate variables 
result = templateString.safe_substitute(
    sidebar = sidebarButtons,
    mobile = mobileSidebar,
    boxes = boxString
)


resultFile = open("generated/website/overviewApplication.html", "w")
resultFile.write(result)
resultFile.close()



# Closing files
fileJson.close()
