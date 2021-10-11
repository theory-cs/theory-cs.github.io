from string import Template
import json
from userFunctions import *
import collections

outcomeData = json.loads(open("outcomes.json").read())

outcome = {}

for big in outcomeData:
  for med in outcomeData[big]['Children']:
    for small in outcomeData[big]['Children'][med]['Children']:
        # print(small)
        outcome[small] = outcomeData[big]['Children'][med]['file']

outcome = collections.OrderedDict(sorted(outcome.items()))
# print(outcome)


content = ""
alphabet = []
for i in outcome:
    # print(i)
    if(i[0] not in alphabet):
        alphabet.append(i[0])

for j in alphabet:
    content += "<h1>" + j + "</h1>\n"
    # print(j)
    for key in outcome:
        # print(key)
        if(key[0] == j):
            content += """<p><a href=\"""" + outcome[key]  + """\">""" + key +"""</a></p>\n"""
    content += "\n"

print(content)

glossaryTemplate = open("templates/glossaryTemplate.html", "r")
templateString = Template(glossaryTemplate.read())

page_variables = site_variables.copy()
page_variables.update(dict(
    content = content
))

#substitute settings unitData with appropriate variables 
result = templateString.substitute(page_variables)


resultFile = open("generated/website/glossary.html", "w")
resultFile.write(result)
resultFile.close()
        
glossaryTemplate.close()

