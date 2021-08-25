from string import Template
import json
  
# Opening JSON file
fileJson = open('unitTemplate.json',)
  
# returns JSON object as a dictionary
data = json.load(fileJson)



sidebarButtons = ""
for i in range(1,len(data)+1):
    sidebarButtons += "<li>"
    sidebarButtons += """<a href= " """ + 'unit'+str(i) + """.html" aria-label="Go to """ + str(i) + """ ">"""
    sidebarButtons += """<i><p class="icons">&nbsp;&nbsp;""" + str(i) + """</p></i>"""
    sidebarButtons += "</a>"
    sidebarButtons += """<span class="tooltip"> """ + str(i) + """</span>"""


#open unitTemplate html file and read it into a string 
sidebarTemplate = open("sidebarTemplate.html", "r")
templateString = Template(sidebarTemplate.read())

#substitute settings data with appropriate variables 
result = templateString.safe_substitute(
    # logoName = title name
    sidebarWeek = sidebarButtons
)


resultFile = open("generated/website/sidebar.html", "w")
resultFile.write(result)
resultFile.close()

fileJson.close()
sidebarTemplate.close()
    
