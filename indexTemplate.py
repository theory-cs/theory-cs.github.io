from string import Template
import json
  
# Opening JSON file
websiteData = json.loads(open("website-settings.json").read())

title = websiteData["Global Class Name"]

copyright = """<div class="copyright">"""
copyright += "Copyright © " + websiteData["Copyright Year"] + websiteData["Copyright Name"] + "<br>"
copyright += """<a style= "color:white;" href="feedback.html">Feedback</a></div>"""

#open indexTemplate html file and read it into a string 
unitTemplate = open("indexTemplate.html", "r")
templateString = Template(unitTemplate.read())

#substitute settings data with appropriate variables 
result = templateString.safe_substitute(
    mainTitle = title,
    copyrightFooter = copyright
)


resultFile = open("generated/website/index.html", "w")
resultFile.write(result)
resultFile.close()

