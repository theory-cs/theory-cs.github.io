from string import Template
import json
from userFunctions import *

# returns unit-settings and websiteData JSON files as dictionaries
unitData = json.loads(open("unit-settings.json").read())
websiteData = json.loads(open("website-settings.json").read())

headerHtml = head("unit")

#adds regular sidebar icons for each of the units/weeks specified in json file
sidebarButtons = sidebar("unit")

#adds mobile sidebar icons for each of the units/weeks specified in json file
mobileSidebar = mobileSidebar("unit")




#big for loop begin
for i in range(0,len(unitData)):
    pdf=""
    tex=""
    html=""

    #extract and format all PDFs and associated buttons
    pdfString="" 
    if('pdfs' in unitData[i]):
        # print("pdfs in "+str(i+1))
        for j in range(len(unitData[i]['pdfs'])):
            if(unitData[i]['pdfs'][j]['addExtensions']):
                #format all filenames 
                pdf= "../output/lessons/"+unitData[i]['pdfs'][j]['file']+".pdf"
                tex= "../notes/lessons/"+unitData[i]['pdfs'][j]['file']+".tex"
                html="../output/lessons/"+unitData[i]['pdfs'][j]['file']+".html"
            else:
                pdf=unitData[i]['pdfs'][j]['file']

            #heading and PDF download button
            pdfString += """<h2 tabindex = "2"> """+ unitData[i]['pdfs'][j]['name'] +"""</h2>
                <a tabindex = "2" class="button PDF" aria-label="Download PDF" href="""+ pdf+ """ download>PDF</a> """
        
            #.tex/.html button
            if( unitData[i]['pdfs'][j]['addExtensions']):
                #.tex
                pdfString += """ <a tabindex = "2" class="button TeX" aria-label="Download .TeX" 
                    href=""" + tex + """ download>TeX</a> """
                #.html
                pdfString += """ <a tabindex = "2" class="button HTML" aria-label="Open HTML file of Document in New Tab" 
                    href= """ + html + """ target="HTML">Raw HTML</a>"""

            #Annotations on/off buttons 
            if('annotatedFile' in unitData[i]['pdfs'][j]):
                pdfString += """ <a tabindex = "2" class="button on" aria-label="Annotations On" id="annotationsOnButton" href="javascript:void(0)" >Annotations On</a>
					<a tabindex = "2" class="button off" aria-label="Annotations Off" id="annotationsOffButton" href="javascript:void(0)" >Annotations Off</a> """

            #annotations on
            pdfString += """ <script> document.getElementById("annotationsOnButton").onclick = function() {annotations(1,
            \""""+pdf+ """\",\"../files/"""+unitData[i]['pdfs'][j]['annotatedFile']+"""\", \""""+unitData[i]['pdfs'][j]['name']+ """\")};"""
            
            #annotations off
            pdfString +="""document.getElementById("annotationsOffButton").onclick = function() {annotations(0,
            \""""+pdf+ """\",\"../files/"""+unitData[i]['pdfs'][j]['annotatedFile']+"""\", \""""+unitData[i]['pdfs'][j]['name']+ """\")};
            </script>"""

            #if addExtensions is false, then the displayed pdf will be in the files directory 
            if(not unitData[i]['pdfs'][j]['addExtensions']): 
                #pdf.js embed from files
                pdfString += """ <br> <iframe class="PDFjs" id=\""""+ unitData[i]['pdfs'][j]['name'] +"""\" src="web/viewer.html?file=../../files/"""+ pdf+ """" 
                    title="webviewer" frameborder="0" width="100%" height="600"></iframe> """
            else:     
                #pdf.js embed default 
                pdfString += """ <br> <iframe class="PDFjs" id=\""""+ unitData[i]['pdfs'][j]['name'] +"""\" src="web/viewer.html?file=../"""+ pdf+ """" 
                title="webviewer" frameborder="0" width="100%" height="600"></iframe> """

        #Information Section
        infoString = ""
        if('Information' in unitData[i]): 
            infoString = "<dl><dt>"+ unitData[i]['Information'][0]+ "</dt>"   
            unitData[i]['Information']                 
            for k in range(1, len(unitData[i]['Information'])) :              
                infoString += "<dd>"+ unitData[i]['Information'][k] +"</dd>"
        infoString += "</dl>"

    #Embedded links section
    embedString = ""
    if('embed' in unitData[i]):
        # print("embed in "+str(i+1))
        for j in range(len(unitData[i]['embed'])): 
            embedString += "<h2>"+unitData[i]['embed'][j]['name']+"</h2>"+ unitData[i]['embed'][j]['embedCode']



    #open unitTemplate html file and read it into a string 
    unitTemplate = open("unitTemplate.html", "r")
    templateString = Template(unitTemplate.read())

    #substitute settings unitData with appropriate variables 
    result = templateString.safe_substitute(
        head = headerHtml,
        heading = unitData[i]['header'],
        Information = infoString, 
        PDF = pdfString,
        embed = embedString,
        sidebar = sidebarButtons,
        mobile = mobileSidebar
    )


    resultFile = open("generated/website/"+'unit'+str(i+1)+".html", "w")
    resultFile.write(result)
    resultFile.close()

#end for loop


# Closing files
unitTemplate.close()
