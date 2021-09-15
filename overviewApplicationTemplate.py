from string import Template
import json
from sidebarFunction import *  

# returns unit-settings JSON file as a dictionary
appData = json.loads(open("applications.json").read())
websiteData = json.loads(open("website-settings.json").read())

#Sidebar top with title of course offering
sidebarButtons = sidebar("application")
            
#Mobile Sidebar top with Title of Course Offering 
mobileSidebar = """ <div id="mySidebar" class="collapsedSidebar">
		<a href="index.html" class="homeMobile"> """ + websiteData['Global Class Name']+"""</a> <!--NAME-->
		<a href="javascript:void(0)" class="closebtn" onclick="closeNav()">×&nbsp;</a>
        <a href="overviewApplication.html">Overview</a>
		"""



#Adds icons in regular sidebar for each 2nd tier child in outcomes.json 
for i in appData:
	file = i.replace(" ", "-").lower()+".html"
	mobileSidebar += """<a href= \"""" + file + """">""" + i + """</a>"""


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


boxString = """<div class="box"> \n"""
#big for loop begin
for i in appData:
	file = i.replace(" ", "-").lower()+".html"
	boxString += """<h2> <i style= "font-size: 75%;" class='bx bxs-chevron-right-square'></i> <a href= \"""" + file + """\" style="color: #182B49; text-decoration: none; font-size: 75%; font-weight: normal;" >""" + i + """</a></h2>"""

boxString += "</div><br><br>"
    
#open unitTemplate html file and read it into a string 
unitTemplate = open("overviewApplicationTemplate.html", "r")
templateString = Template(unitTemplate.read())

#substitute settings appData with appropriate variables 
result = templateString.safe_substitute(
    sidebar = sidebarButtons,
    mobile = mobileSidebar,
    boxes = boxString
)


resultFile = open("generated/website/overviewApplication.html", "w")
resultFile.write(result)
resultFile.close()

unitTemplate.close()
