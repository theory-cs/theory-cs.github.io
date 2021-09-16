from string import Template
import json
from userFunctions import *
  
# Opening JSON file
websiteData = json.loads(open("website-settings.json").read())



feedback = """<div class="feedback_form">"""
feedback += websiteData["Feedback"]
feedback += "</div>"


copyright = """<div class="copyright">"""
copyright += "Copyright © " + websiteData["Copyright Year"] + " " + websiteData["Copyright Name"] + "<br>"
copyright += """<a style= "color:white;" href="feedback.html">Feedback</a></div>"""


#open indexTemplate html file and read it into a string 
unitTemplate = open("templates/feedbackTemplate.html", "r")
templateString = Template(unitTemplate.read())

page_variables = site_variables.copy()
page_variables.update(dict(
    feedbackForm = feedback,
    copyrightFooter = copyright
))
#substitute settings data with appropriate variables 
result = templateString.substitute(page_variables)

resultFile = open("generated/website/feedback.html", "w")
resultFile.write(result)
resultFile.close()

