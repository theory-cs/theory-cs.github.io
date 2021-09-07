from string import Template
import json
  
# Opening JSON file
fileJson = open('unitTemplate.json',)
  
# returns JSON object as a dictionary
data = json.load(fileJson)

sidebarButtons = ""
for i in range(1,len(data)+1):
    sidebarButtons += "<li>"
    sidebarButtons += """<a href= " """ + 'unit'+str(i) + """.html" aria-label="Go to """ + data['unit'+str(i)]['header'] + """ ">"""
    sidebarButtons += """<i><p class="icons">&nbsp;&nbsp;&nbsp;&nbsp;""" + str(i) + """</p></i>"""
    sidebarButtons += """<span class="links_name"> """ + data['unit'+str(i)]['header'] + """</span>"""
    sidebarButtons += "</a>"
    sidebarButtons += """<span class="tooltip"> """ + data['unit'+str(i)]['header'] + """</span>"""
    sidebarButtons += "</li>"

mobileSidebar = ""
for i in range(1,len(data)+1):
   mobileSidebar += """<a href= \"""" + 'unit'+str(i) + """.html\"">""" + data['unit'+str(i)]['header'] + """</a>"""

#open unitTemplate html file and read it into a string 
unitTemplate = open("overviewCalendarTemplate.html", "r")
templateString = Template(unitTemplate.read())

#substitute settings data with appropriate variables 
result = templateString.safe_substitute(   
    sidebar = sidebarButtons,
    mobile = mobileSidebar
)


resultFile = open("generated/website/overview.html", "w")
resultFile.write(result)
resultFile.close()

# Closing files
fileJson.close()
unitTemplate.close()
