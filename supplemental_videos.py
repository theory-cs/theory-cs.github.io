from os import remove
from string import Template
import json
from user_functions import *
from create_zip import *

# returns unit_settings JSON file as a dictionary
unitData = json.loads(open("unit_settings.json").read())
websiteSettings = json.loads(open("website-settings.json").read())

titleArray = []
idArray = []
embedString = ""
podcast = "<p> Podcast from this quarter: <a href =" + websiteData["Podcast"] + ">link</a>\n</p>"

# Get all YouTube embed
for i in range(0,len(unitData)):
    if('content' in unitData[i]):
        for j in range(len(unitData[i]['content'])):
            if(("https://youtu.be" in unitData[i]['content'][j]['source'][:16] ) or ("https://www.youtube" in unitData[i]['content'][j]['source'][:19] )):
                youtubeEmbedLink = unitData[i]['content'][j]['source'].replace("https://youtu.be/","").replace("https://www.youtube.com/embed/","")
                embedID =  unitData[i]['content'][j]['source'].replace(" ","-")
                embedString += "<h2 id=\""+embedID+"\">"+unitData[i]['content'][j]['name']+"</h2>"
                titleArray.append(unitData[i]['content'][j]['name'])
                idArray.append(embedID)
                embedString += "<iframe height=\"600px\" width=\"100%\" src=\"https://www.youtube.com/embed/"+youtubeEmbedLink+"\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>"

# Overview on top
overview = ""
for m in range(0, len(titleArray)):
    overview += "<p> "
    overview += """<a href=\"supplemental_videos.html#""" + idArray[m] + """\">"""
    overview += titleArray[m]
    overview += " </a>"
    overview += " </p>\n"

embedString = podcast + overview + embedString

supplemental_videos_template = open("templates/supplemental_videos_template.html", "r")
templateString = Template(supplemental_videos_template.read())

page_variables = site_variables.copy()
page_variables.update(dict(
    heading = unitData[i]['header'],
    youtubelinks = embedString
))

# Substitute settings unitData with appropriate variables 
result = templateString.substitute(page_variables)

write_if_different("generated/website/supplemental_videos.html", result)

# Closing files
supplemental_videos_template.close()
        