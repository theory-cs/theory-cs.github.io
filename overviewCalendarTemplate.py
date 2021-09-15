from string import Template
import json
from sidebarFunction import *
  
# returns unit-settings JSON file as a dictionary
unitData = json.loads(open("unit-settings.json").read())
websiteData = json.loads(open("website-settings.json").read())

#Sidebar top with title of course offering
sidebarButtons = sidebar("unit")

#Mobile Sidebar top with Title of Course Offering 
mobileSidebar = """ <div id="mySidebar" class="collapsedSidebar">
		<a href="index.html" class="homeMobile"> """ + websiteData['Course Offering Title']+"""</a> <!--NAME-->
		<a href="javascript:void(0)" class="closebtn" onclick="closeNav()">×&nbsp;</a>
			
		<a href="overviewCalendar.html">Calendar</a>"""

# Generate mobile sidebar buttons
for i in range(0,len(unitData)):
   mobileSidebar += """<a href= \"""" + 'unit'+str(i+1) + """.html\"">""" + unitData[i]['header'] + """</a>"""

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


# Open unitTemplate html file and read it into a string 
unitTemplate = open("overviewCalendarTemplate.html", "r")
templateString = Template(unitTemplate.read())

# Substitute settings unitData with appropriate variables 
result = templateString.safe_substitute(   
    sidebar = sidebarButtons,
    mobile = mobileSidebar
)


resultFile = open("generated/website/overviewCalendar.html", "w")
resultFile.write(result)
resultFile.close()

# Close files
unitTemplate.close()
