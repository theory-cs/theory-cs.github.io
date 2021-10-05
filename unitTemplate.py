from string import Template
import json
from userFunctions import *

# returns unit-settings JSON file as a dictionary
unitData = json.loads(open("unit-settings.json").read())

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
                tex= "../notes/lessons-flat/"+unitData[i]['pdfs'][j]['file']+".tex"
                html="../output/lessons/"+unitData[i]['pdfs'][j]['file']+".html"
            else:
                pdf=unitData[i]['pdfs'][j]['file']

            #heading and PDF download button
            pdfString += """<h2 tabindex = "2"> """+ unitData[i]['pdfs'][j]['name'] +"""</h2>
                <a tabindex = "2" class="button PDF" aria-label="Download PDF" href="""+ pdf+ """ download>PDF</a> """
        
            #.tex/.html button
            if( unitData[i]['pdfs'][j]['addExtensions']):
                #.tex
                pdfString += """ <a tabindex = "2" class="button LaTeX" aria-label="Download .LaTeX" 
                    href=""" + tex + """ download>LaTeX</a> """
                #.html
                pdfString += """ <a tabindex = "2" class="button HTML" aria-label="Open HTML file of Document in New Tab" 
                    href= """ + html + """ target="HTML">Raw HTML</a>"""

            pdfjsID =""
            #Annotations on/off buttons 
            if('annotatedFile' in unitData[i]['pdfs'][j]):
                pdfString += """ <a tabindex = "2" class="button on" aria-label="Annotations On" id="annotationsOnButton" href="javascript:void(0)" >Annotations On</a>
					<a tabindex = "2" class="button off" aria-label="Annotations Off" id="annotationsOffButton" href="javascript:void(0)" >Annotations Off</a> """

                #id of pdf.js element formatting
                pdfjsID = unitData[i]['pdfs'][j]['name'].replace(" ", "-")
                #annotations on
                pdfString += """ <script> document.getElementById("annotationsOnButton").onclick = function() {annotations(1,
                \""""+pdf+ """\",\"../files/"""+unitData[i]['pdfs'][j]['annotatedFile']+"""\", \""""+pdfjsID+ """\")};"""
            
                #annotations off
                pdfString +="""document.getElementById("annotationsOffButton").onclick = function() {annotations(0,
                \""""+pdf+ """\",\"../files/"""+unitData[i]['pdfs'][j]['annotatedFile']+"""\", \""""+pdfjsID+ """\")};
                </script>"""

            #if addExtensions is false, then the displayed pdf will be in the files directory 
            if(not unitData[i]['pdfs'][j]['addExtensions']): 
                #pdf.js embed from files
                pdfString += """ <br> <iframe class="PDFjs" id=\""""+ pdfjsID +"""\" src="web/viewer.html?file=../../files/"""+ pdf+ """" 
                    title="webviewer" frameborder="0" width="100%" height="600"></iframe> """
            else:     
                #pdf.js embed default 
                pdfString += """ <br> <iframe class="PDFjs" id=\""""+ pdfjsID +"""\" src="web/viewer.html?file=../"""+ pdf+ """" 
                title="webviewer" frameborder="0" width="100%" height="600"></iframe> """

        #Information Section
        infoString = ""
        if('CalendarInfo' in unitData[i]): 
            infoString = "<dl><dt>" + unitData[i]['CalendarInfo'] + "</dt></dl>"
#            infoString = "<dl><dt>"+ unitData[i]['calendarInfo'][0]+ "</dt>"   
#            unitData[i]['calendarInfo']                 
#            for k in range(1, len(unitData[i]['calendarInfo'])) :              
#                infoString += "<dd>"+ unitData[i]['calendarInfo'][k] +"</dd>"
#        infoString += "</dl>"

    #Embedded links section
    embedString = ""
    if('embed' in unitData[i]):
        # print("embed in "+str(i+1))
        for j in range(len(unitData[i]['embed'])):
            embedID =  unitData[i]['embed'][j]['name'].replace(" ","-")
            embedString += "<h2 id=\""+embedID+"\">"+unitData[i]['embed'][j]['name']+"</h2>"+ unitData[i]['embed'][j]['embedCode']



    #open unitTemplate html file and read it into a string 
    unitTemplate = open("templates/unitTemplate.html", "r")
    templateString = Template(unitTemplate.read())

    page_variables = site_variables.copy()
    page_variables.update(dict(
        heading = unitData[i]['header'],
        Information = infoString, 
        PDF = pdfString,
        embed = embedString
    ))

    #substitute settings unitData with appropriate variables 
    result = templateString.substitute(page_variables)


    resultFile = open("generated/website/"+'unit'+str(i+1)+".html", "w")
    resultFile.write(result)
    resultFile.close()

#end for loop


# Closing files
unitTemplate.close()
