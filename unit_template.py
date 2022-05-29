from os import remove
from string import Template
import json
from user_functions import *
from create_zip import *
from os.path import exists

# returns unit_settings JSON file as a dictionary
unitData = json.loads(open("unit_settings.json").read())

# returns website-settings JSON file as a dictionary
websiteData = json.loads(open("website-settings.json").read())

#big for loop begin
for i in range(0,len(unitData)):
    pdf=""
    tex=""
    html=""
    embedString = ""
    #extract and format all PDFs and associated buttons
    pdfString=""
    if('content' in unitData[i]):
        # print("pdfs in "+str(i+1))
        elementCount = 0
        for j in range(len(unitData[i]['content'])):
            elementCount +=1; 

            #if source value ends with .tex extension, add pdf and html versions, and 
            #create zip file of .tex file with its accompanying images 
            if(unitData[i]['content'][j]['source'][-4:] == '.tex'):
                #format all filenames 
                tex = ""
                pdf = "../output/lessons/"+unitData[i]['content'][j]['source'].replace(".tex",".pdf")
                html = "../output/lessons/"+unitData[i]['content'][j]['source'].replace(".tex",".html")
                
                #create zip files 
                tex = zip_file(unitData[i]['content'][j]['source'].replace(".tex",""), "lessons-flat")
                if(tex == None):
                    tex=""

                #heading and PDF download button, only PDF download button in this case 
                pdfString += """<h2 tabindex = "2"> """+ unitData[i]['content'][j]['name'] +"""</h2>
                <a tabindex = "2" class="button PDF" aria-label="Download PDF" href="""+ pdf+ """ download>PDF</a> """
                #.tex
                pdfString += """ <a tabindex = "2" class="button LaTeX" aria-label="Download .LaTeX" 
                    href=""" + tex + """ download>LaTeX</a> """
                #.html
                pdfString += """ <a tabindex = "2" class="button HTML" aria-label="Open HTML file of Document in New Tab" 
                    href= """ + html + """ target="HTML">Raw HTML</a><span style="font-weight: bold;
					font-size: 100%;">&nbsp&nbsp&nbsp&nbsp Annotations</span>"""
                
               

                #id of pdf.js element formatting
                pdfjsID = unitData[i]['content'][j]['source'].replace(" ", "-")

                #annotatedFileName will be as such: for Week4.tex -> Week4-annotated.pdf
                annotatedFileName= unitData[i]['content'][j]['source'].replace(".tex","")
                annotatedFileName = annotatedFileName+websiteData["Annotated"]+".pdf"

                if(exists("files/"+annotatedFileName)):
                    #annotations switch/toggle
                    pdfString += """
                    <label class="switch">
                    <input type="checkbox" id="toggle-"""+str(elementCount)+"""">
                    <span class="slider round"></span>
                    </label>
                    """
                    
                    #annotations on
                    pdfString += """ <script> document.getElementById("toggle-"""+str(elementCount)+"""").onclick = function() {annotations(
                     """+str(elementCount)+""", \""""+pdf+ """\",\"../files/"""+annotatedFileName+"""\", \""""+pdfjsID+ """\")}; </script>"""
                
                #pdf.js embed default 
                pdfString += """ <br> <iframe class="PDFjs" id=\""""+ pdfjsID +"""\" src="web/viewer.html?file=../"""+ pdf+ """" 
                title="webviewer" frameborder="0" width="100%" height="600"></iframe> """
            
            #if source value ends with .pdf, refer to the files directory  
            elif (unitData[i]['content'][j]['source'][-4:] == '.pdf'):
                pdf="../files/"+unitData[i]['content'][j]['source']

                #heading and PDF download button, only PDF download button in this case 
                pdfString += """<h2 tabindex = "2"> """+ unitData[i]['content'][j]['name'] +"""</h2>
                <a tabindex = "2" class="button PDF" aria-label="Download PDF" href="""+ pdf+ """ download>PDF</a> """

                pdfjsID = unitData[i]['content'][j]['source'].replace(" ", "-")
                
            
                #annotatedFileName will be as such: for Week4.tex -> Week4-annotated.pdf
                annotatedFileName= unitData[i]['content'][j]['source'].replace(".pdf","")
                annotatedFileName = annotatedFileName+websiteData["Annotated"]+".pdf"
                
                if(exists("files/"+annotatedFileName)):
                    pdfString += """<div style="font-weight: 700; font-size: 120%; display: inline-block;">&nbsp&nbspAnnotations:&nbsp</div><label class="toggle">
                                <span class="onoff">OFF</span>
                                            <input type="checkbox" />
                        <span class="slider round" id="annotationsOnButton"""+str(elementCount)+""""></span>
                        </label> <br>"""
                    
                   
                    #annotations on
                    pdfString += """ <script> document.getElementById("annotationsOnButton"""+str(elementCount)+"""").onclick = function() {annotations("""+str(elementCount)+""", 
                     \""""+pdf+ """\",\"../files/"""+annotatedFileName+"""\", \""""+pdfjsID+ """\")}; </script>"""

                #pdf.js embed from files
                pdfString += """ <br> <iframe class="PDFjs" id=\""""+ pdfjsID +"""\" src="web/viewer.html?file=../../files/"""+ pdf+ """" 
                    title="webviewer" frameborder="0" width="100%" height="600"></iframe> """
            
            
            #if source value is a youtube link, embed it  
            elif(("https://youtu.be" in unitData[i]['content'][j]['source'][:16] ) or 
                ("https://www.youtube" in unitData[i]['content'][j]['source'][:19] )):
                
                youtubeEmbedLink = unitData[i]['content'][j]['source'].replace("https://youtu.be/","").replace("https://www.youtube.com/embed/","")
                # print(youtubeEmbedLink)
                embedID =  unitData[i]['content'][j]['source'].replace(" ","-")
                embedString += "<h2 id=\""+embedID+"\">"+unitData[i]['content'][j]['name']+"</h2>"
                embedString += "<iframe height=\"600px\" width=\"100%\" src=\"https://www.youtube.com/embed/"+youtubeEmbedLink+"\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>"
                # print("src=\"https://www.youtube.com/embed/"+unitData[i]['embedYoutube'][j]['link']+"\"")

            #else embed directly    
            else : 
                embedID =  unitData[i]['content'][j]['name'].replace(" ","-")
                embedString += "<h2 id=\""+embedID+"\">"+unitData[i]['content'][j]['name']+"</h2>"+ unitData[i]['content'][j]['source']+"\n"
       

            
            
            
            
            
        




        #Information Section
        infoString = ""
        if('CalendarInfo' in unitData[i]): 
            infoString = "<dl><dt>" + unitData[i]['CalendarInfo'] + "</dt></dl>"

    #open unit_template html file and read it into a string 
    unit_template = open("templates/unit_template.html", "r")
    templateString = Template(unit_template.read())

    page_variables = site_variables.copy()
    page_variables.update(dict(
        heading = unitData[i]['header'],
        Information = infoString, 
        PDF = pdfString,
        embed = embedString
    ))

    #substitute settings unitData with appropriate variables 
    result = templateString.substitute(page_variables)

    write_if_different("generated/website/"+'unit'+str(i+1)+".html", result)

#end for loop


#Closing files
unit_template.close()