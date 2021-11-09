from os import remove
from string import Template
import json
from user_functions import *
from create_zip import *

# returns unit-settings JSON file as a dictionary
unitData = json.loads(open("unit-settings.json").read())


embedString = ""
for i in range(0,len(unitData)):

    if('embedYoutube' in unitData[i]):
        for j in range(len(unitData[i]['embedYoutube'])):
            youtubeEmbedLink = unitData[i]['embedYoutube'][j]['link'].replace("https://youtu.be/","").replace("https://www.youtube.com/embed/","")
            # print(youtubeEmbedLink)
            embedID =  unitData[i]['embedYoutube'][j]['name'].replace(" ","-")
            embedString += "<h2 id=\""+embedID+"\">"+unitData[i]['embedYoutube'][j]['name']+"</h2>"
            embedString += "<iframe height=\"600px\" width=\"100%\" src=\"https://www.youtube.com/embed/"+youtubeEmbedLink+"\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>"
            # print("src=\"https://www.youtube.com/embed/"+unitData[i]['embedYoutube'][j]['link']+"\"")

print(embedString)

youtube_template = open("templates/youtube_template.html", "r")
templateString = Template(youtube_template.read())

page_variables = site_variables.copy()
page_variables.update(dict(
    heading = unitData[i]['header'],
    youtubelinks = embedString
))

#substitute settings unitData with appropriate variables 
result = templateString.substitute(page_variables)


resultFile = open("generated/website/youtube_links.html", "w")
resultFile.write(result)
resultFile.close()

#end for loop


# Closing files
youtube_template.close()
        