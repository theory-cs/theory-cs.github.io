from string import Template
import json
from user_functions import *
from create_zip import *
  
# returns unit_settings JSON file as a dictionary
appData = json.loads(open("applications.json").read())

for (k,v) in appData.items():
    #extract and format all PDFs and associated buttons
    file = k.replace(" ", "-").lower()

    pdfString = ""
    collapseVar = 1

    #format pdf/html/tex file names
    pdf="../output/app/"+file+".pdf"
    html="../output/app/"+file+".html"
    #where will tex file for applications be shown? 
    print("file: "+file)
    tex= zip_file(file, "app-flat")
    #print(tex)

    #TODO: comment when this condition is happening 
    if(tex == None):
        tex=""
            
    #.pdf Download button
    pdfString += """ <p> <a tabindex = "2" class="button PDF" aria-label="Download PDF" 
    href="""+pdf+""" download>PDF</a>"""

    #.tex Download button
    pdfString += """ <a tabindex = "2" class="button LaTeX" aria-label="Download .LaTeX" 
    href=""" + tex + """ download>LaTeX</a> """

    #Raw HTML button 
    pdfString += """ <a tabindex = "2" class="button HTML" aria-label="Open HTML file of Document in New Tab" 
    href= """ + html + """ target="HTML">Raw HTML</a>"""
        
    #pdf.js embed 
    pdfString += """ <br> <iframe class="PDFjs" id=\""""+ k +"""\" src="web/viewer.html?file=../"""+ pdf+ """" 
    title="webviewer" frameborder="0" width="100%" height="600"></iframe> """
            
    #increment collapseVar
    collapseVar += 1
    
    #open app_template html file and read it into a string 
    app_template = open("templates/app_template.html", "r")
    templateString = Template(app_template.read())

    page_variables = site_variables.copy()
    page_variables.update(dict(
        heading = k,
        collapsibleMenu = pdfString
    ))

    #substitute settings appData with appropriate variables 
    result = templateString.substitute(page_variables)

    write_if_different("generated/website/" + file + ".html", result)

#end for loop


# Closing files
app_template.close()