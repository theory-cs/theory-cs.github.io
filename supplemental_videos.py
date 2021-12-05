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
for i in range(0,len(unitData)):
    if('embedYoutube' in unitData[i]):
        for j in range(len(unitData[i]['embedYoutube'])): 
            titleArray.append(unitData[i]['embedYoutube'][j]['name'])
            embedID =  unitData[i]['embedYoutube'][j]['name'].replace(" ","-")
            idArray.append(embedID)

# print(titleArray)
# print(idArray)

# Alphabetical view on top
embedString = ""

embedString += "<p> Podcast: <a href =" + websiteData["Podcast"] + ">link</a>\n</p>"
for i in range(0, len(titleArray)):
    embedString += "<p> "
    embedString += """<a href=\"supplemental_videos.html#""" + idArray[i] + """\">"""
    embedString += titleArray[i]
    embedString += " </a>"
    embedString += " </p>\n"




for i in range(0,len(unitData)):

    if('embedYoutube' in unitData[i]):
        for j in range(len(unitData[i]['embedYoutube'])):
            youtubeEmbedLink = unitData[i]['embedYoutube'][j]['link'].replace("https://youtu.be/","").replace("https://www.youtube.com/embed/","")
            # print(youtubeEmbedLink)
            embedID =  unitData[i]['embedYoutube'][j]['name'].replace(" ","-")
            embedString += "<h2 id=\""+embedID+"\">"+unitData[i]['embedYoutube'][j]['name']+"</h2>"
            embedString += "<iframe height=\"600px\" width=\"100%\" src=\"https://www.youtube.com/embed/"+youtubeEmbedLink+"\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>"
            # print("src=\"https://www.youtube.com/embed/"+unitData[i]['embedYoutube'][j]['link']+"\"")

# print(embedString)

supplemental_videos_template = open("templates/supplemental_videos_template.html", "r")
templateString = Template(supplemental_videos_template.read())

page_variables = site_variables.copy()
page_variables.update(dict(
    heading = unitData[i]['header'],
    youtubelinks = embedString
))

#substitute settings unitData with appropriate variables 
result = templateString.substitute(page_variables)


write_if_different("generated/website/supplemental_videos.html", result)

#end for loop


# Closing files
supplemental_videos_template.close()
        