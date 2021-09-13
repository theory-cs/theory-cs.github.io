from string import Template
import json
  
# returns unit-settings JSON file as a dictionary
appData = json.loads(open("applications.json").read())
websiteData = json.loads(open("website-settings.json").read())

#Sidebar top with title of course offering
sidebarButtons = """<div class="sidebar">
		<div class="logo-details">
		  
		    <div class="logo_name"><i class='bx bx-home-smile'></i> </div>
			<a href="index.html" class="logo_name">""" + websiteData['Global Class Name']+"""</a> <!--NAME-->
			<i class='bx bx-chevron-right' id="btn" ></i>
		</div>

		<ul class="nav-list">
			
			<li>
				<a href="overviewApplication.html" aria-label="Go to Overview">
					<i class='bx bx-list-ul'></i>
					<span class="links_name">Overview</span>
				</a>
				<span class="tooltip">Overview</span>
			</li>"""



#adds regular sidebar icons for each of the applications specified in json file
for i in appData:
    file = i.replace(" ", "-").lower()+".html"
    sidebarButtons += "<li>"
    sidebarButtons += """<a href= \"""" + file + """\" aria-label="Go to """ + i + """ ">"""
    sidebarButtons += """<i><p class="icons">&nbsp;&nbsp;""" + appData[i]['Icon'] + """</p></i>"""
    sidebarButtons += """<span class="links_name"> """ + i + """</span>"""
    sidebarButtons += "</a>"
    sidebarButtons += """<span class="tooltip"> """ + i + """</span>"""
    sidebarButtons += "</li>"


#end div tags and script for sidebar
sidebarButtons += """</ul> </div> 
	<script>
		let sidebar = document.querySelector(".sidebar");
		let closeBtn = document.querySelector("#btn");
		
		closeBtn.addEventListener("click", ()=>{
			sidebar.classList.toggle("open");
			menuBtnChange();//calling the function(optional)
		});
		
		searchBtn.addEventListener("click", ()=>{ // Sidebar open when you click on the search iocn
			sidebar.classList.toggle("open");
			menuBtnChange(); //calling the function(optional)
		});
		
		// following are the code to change sidebar button(optional)
		function menuBtnChange() {
			if(sidebar.classList.contains("open")){
				closeBtn.classList.replace("bx-chevron-right", "bx-chevron-left");//replacing the iocns class
			}
			else {
				closeBtn.classList.replace("bx-chevron-left","bx-chevron-right");//replacing the iocns class
			}
		}
	</script>"""

#Mobile Sidebar top with Title of Course Offering 
mobileSidebar = """ <div id="mySidebar" class="collapsedSidebar">
		<a href="index.html" class="homeMobile"> """ + websiteData['Global Class Name']+"""</a> <!--NAME-->
		<a href="javascript:void(0)" class="closebtn" onclick="closeNav()">×&nbsp;</a>
        <a href="overviewApplication.html">Overview</a>
		"""


#adds regular mobile icons for each of the applications specified in json file
for i in appData:
    file = i.replace(" ", "-").lower()+".html"
    mobileSidebar += """<a href= \"""" + file + """\"">""" + i + """</a>"""

#end div tags, open button, and script for mobile sidebar 
mobileSidebar += """</div> <br>
	<div class="openbutton" style="margin-left: 10px;">
		<button class="openbtn"  onclick="openNav()">☰ Open Sidebar</button> <br><br>
	</div> 
    <script>
		function openNav() {
			document.getElementById("mySidebar").style.width = "100%";
			document.getElementById("content").style.marginLeft = "100%";
		}
				  
		function closeNav() {
			document.getElementById("mySidebar").style.width = "0";
			document.getElementById("content").style.marginLeft= "0";
		}
	</script> """

for (k,v) in appData.items():
    #extract and format all PDFs and associated buttons
    file = k.replace(" ", "-").lower()

    pdfString = ""
    collapseVar = 1

    #format pdf/html/tex file names
    pdf="../output/"+file+".pdf"
    html="../output/"+file+".html"
    #where will tex file for applications be shown? 
    tex="../notes/"+file+".tex"

    #heading and collapsible card stuff
    pdfString += """<div class="card"> <div class="card-header"> <a class="card-link" data-toggle="collapse" 
    href="#collapse"""+ str(collapseVar)+"\"> "+k+"""</a> </div> <div id="collapse""" + str(collapseVar)+ """""
    class="collapse" data-parent="#accordion"><div class="card-body">"""
            
    #Learning Goal
    #pdfString += """ <p> Learning Goal: """+ appData[i]['Children'][j]['Children'][k]['Description']+"""</p>"""
            
    #.pdf Download button
    pdfString += """ <p> <a tabindex = "2" class="button PDF" aria-label="Download PDF" 
    href="""+pdf+""" download>PDF</a>"""

    #.tex Download button
    pdfString += """ <a tabindex = "2" class="button TeX" aria-label="Download .TeX" 
    href=""" + tex + """ download>TeX</a> """
        
    #Open in Overleaf button
    # pdfString += """ <a tabindex = "2" class="button Overleaf" aria-label="Open in Overleaf" 
    # href= """ + appData[i]['Children'][k]['overleaf']+ """ target="Overleaf">Overleaf</a> """

    #Raw HTML button 
    pdfString += """ <a tabindex = "2" class="button HTML" aria-label="Open HTML file of Document in New Tab" 
    href= """ + html + """ target="HTML">Raw HTML</a>"""
        
    #pdf.js embed 
    pdfString += """ <br> <iframe class="PDFjs" id=\""""+ k +"""\" src="web/viewer.html?file="""+ pdf+ """" 
    title="webviewer" frameborder="0" width="100%" height="600"></iframe> """

    #closing div for collapsible menu item 
    pdfString += """</div></div></div>"""
            
    #increment collapseVar
    collapseVar += 1

   #Information Section
    #infoString = "<p>"+ appData[i]['Children'][j]['Description']+ "</p>" 
    
    
    #open unitTemplate html file and read it into a string 
    appTemplate = open("appTemplate.html", "r")
    templateString = Template(appTemplate.read())

    #substitute settings appData with appropriate variables 
    result = templateString.safe_substitute(
    heading = k,
    #Information = infoString, 
    collapsibleMenu = pdfString,
    sidebar = sidebarButtons,
    mobile = mobileSidebar
    )


    resultFile = open("generated/website/"+file+".html", "w")
    resultFile.write(result)
    resultFile.close()

#end for loop


# Closing files
appTemplate.close()