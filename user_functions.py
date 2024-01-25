from string import Template
import json
from create_zip import *

websiteData = json.loads(open("website-settings.json").read())


# "application" | "unit" | "outcome" -> HTML (for the sidebar)
def build_sidebar(titleHref, titleName, overviewHref, overviewName, overviewIcon, buttonsContent, smallWidth):
	sidebarButtons = """ <div class="sidebar\""""
	#unit view must have smaller width
	if(smallWidth):
		sidebarButtons+= """id=\"unit\""""
	sidebarButtons+=""">"""
	
	sidebarButtons += """
		<li><a href= " courseInfo.html" aria-label="Go to Home "><i class='bx bx-home-smile'></i><span class="links_name"> Home</span></a><span class="tooltip"> Home</span></li>
	"""

	sidebarButtons += """
			
			<ul class="nav-list">
			
			<li>
				<a href=""" + overviewHref + """ aria-label="Go to""" + overviewName + """\">
					<i class=""" + overviewIcon + """></i>
					<span class="links_name">""" + overviewName + """</span>
				</a>
				<span class="tooltip">""" + overviewName + """</span>
			</li>"""

		

	sidebarButtons += buttonsContent

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
	
	return sidebarButtons


def build_mobile_sidebar(titleHref, titleName, overviewHref, overviewName, mobileButtonsContent):
	mobileSidebarButtons = """ <div id="mySidebar" class="collapsedSidebar">
			<a href=""" + titleHref + """ class="homeMobile"> """ + titleName +"""</a> <!--NAME-->
		  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">×&nbsp;</a>
			<a href=""" + overviewHref + """>""" + overviewName + """</a>"""
	
	mobileSidebarButtons += mobileButtonsContent
		

	mobileSidebarButtons += """ </div>

		<div class="openbutton">
			<button class="openbtn"  onclick="openNav()">☰ Menu</button> 
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
		</script>
		"""

	return mobileSidebarButtons

def build_head_html(title):
	headHtml = """<head>
	<!-- logo on tab-->
	<link rel="shortcut icon" href="../resources/images/wood-951875_960_720.jpeg" type="image/x-icon">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="google-site-verification" content="Cn_GGElo-cbNkuj65G4fN_F-MR20NoOdTx_rlckOEPU" />

    <!-- import font -->
	<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200&display=swap" rel="stylesheet">
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>	
	
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="description" content="Introduction to Theory of Computation">
	<meta name="author" content="Mia Minnes">

	<title>""" + title + """</title>

	<!-- Bootstrap Core CSS -->
	<link rel="stylesheet" href="css/bootstrap.min.css">

	<!---Collapsible Menu-->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

	<link rel="stylesheet" href="css/sidebarStyle.css">
	<link rel="stylesheet" href="css/style.css">


	<!-- icons for side menu -->
	<link rel='stylesheet' href='https://unpkg.com/boxicons@2.0.7/css/boxicons.min.css' >
	<link rel="shortcut icon" href="../resources/images/wood-951875_960_720.jpeg" type="image/x-icon">
</head>
	"""
	return headHtml


# Application
appData = json.loads(open("applications.json").read())
appButtonsContent = ""
for i in appData:
	file = i.replace(" ", "-").lower()+".html"
	appButtonsContent += "<li>"
	appButtonsContent += """<a href= \"""" + file + """\" aria-label="Go to """ + i + """ ">"""
	appButtonsContent += """<i><p class="icons">&nbsp;&nbsp;""" + appData[i]['Icon'] + """</p></i>"""
	appButtonsContent += """<span class="links_name"> """ + i + """</span>"""
	appButtonsContent += "</a>"
	appButtonsContent += """<span class="tooltip"> """ + i + """</span>"""
	appButtonsContent += "</li>\n"

appMobileButtonsContent = ""
for i in appData:
	file = i.replace(" ", "-").lower()+".html"
	appMobileButtonsContent += """<a href= \"""" + file + """\">""" + i + """</a>\n"""



# Outcome
outcomeData = json.loads(open("outcomes.json").read())
outcomeButtonsContent = ""
for big in outcomeData:
	for med in outcomeData[big]['Children']:
		#only put icon in sidebar of 2nd tier outcomes that have children 
		if(bool(outcomeData[big]['Children'][med]['Children'])):
			outcomeButtonsContent += "<li>"
			outcomeButtonsContent += """<a href= \"""" +outcomeData[big]['Children'][med]['file'] + """?box=1\" aria-label="Go to """ + med + """ ">"""
			outcomeButtonsContent += """<i><p class="icons">&nbsp;&nbsp;""" + outcomeData[big]['Children'][med]['Icon'] + """</p></i>"""
			outcomeButtonsContent += """<span class="links_name"> """ + med + """</span>"""
			outcomeButtonsContent += "</a>"
			outcomeButtonsContent += """<span class="tooltip"> """ + med + """</span>"""
			outcomeButtonsContent += "</li>\n"

outcomeMobileButtonsContent = ""
for big in outcomeData:
	for med in outcomeData[big]['Children']:
		#only put icon in sidebar of 2nd tier outcomes that have children 
		if(bool(outcomeData[big]['Children'][med]['Children'])):
			outcomeMobileButtonsContent += """<a href= \"""" + outcomeData[big]['Children'][med]['file'] + """\"">""" + med + """</a>"""


# Unit
unitData = json.loads(open("unit_settings.json").read())
assignmentData = json.loads(open("assignments.json").read()) #assignment information displays on calendar
sidebarButtonsUnitData = json.loads(open("sidebar_buttons_unit.json").read())

def secondaryUnitBoxes():
	#content for the non-mobile secondary unit sidebar (will have all of the weeks)
	secondaryUnitButtonsContent = """<div class="sidebar secondary"id="unit2" style="margin-left: 78px; width: 70px">
			<ul class="nav-list" style="margin-top: 100px"> """

	for i in range(0,len(unitData)):
		secondaryUnitButtonsContent += "<li>"
		secondaryUnitButtonsContent += """<a href= " """ + 'unit'+str(i+1) + """.html" aria-label="Go to """ + unitData[i]['header'] + """ ">"""
		secondaryUnitButtonsContent += """<i><p class="icons">&nbsp;&nbsp;&nbsp;&nbsp;""" + str(i+1) + """</p></i>"""
		secondaryUnitButtonsContent += """<span class="links_name"> """ + unitData[i]['header'] + """</span>"""
		secondaryUnitButtonsContent += "</a>"
		secondaryUnitButtonsContent += """<span class="tooltip"> """ + unitData[i]['header'] + """</span>"""
		secondaryUnitButtonsContent += "</li>"

	secondaryUnitButtonsContent += "</ul> </div>"
	return secondaryUnitButtonsContent

#print("TWO "+secondaryUnitBoxes())

#MOBILE SIDEBAR!! 
unitMobileButtonsContent = ""
#another for loop for non-week links in sidebar_buttons_unit.json
unitMobileButtonsContent += "<a href=\"assignments.html\"> Assignments </a>"
unitMobileButtonsContent += "<a href=\"glossary.html\"> Glossary </a>"
unitMobileButtonsContent += "<a href=\"supplemental_videos.html\"> Supplemental Videos </a>"
unitMobileButtonsContent += "<a href=\"office_hours.html\"> Office Hours </a>"
for i in range(0,len(unitData)):
	unitMobileButtonsContent += """<a href= \"""" + 'unit'+str(i+1) + """.html\"">""" + unitData[i]['header'] + """</a>"""

#Primary Unit Sidebar (Non-week links)
sidebarUnitButtonsContent = ""

for element in sidebarButtonsUnitData:
	link = element[0]
	icon = element[1]
	name = link.replace("_"," ").replace(".html","").title()
	
	sidebarUnitButtonsContent += "<li>"
	sidebarUnitButtonsContent += """<a href= " """ + link + """" aria-label="Go to """ +name + """ ">"""
	sidebarUnitButtonsContent += """<i class='"""+icon+"""'></i>"""
	sidebarUnitButtonsContent += """<span class="links_name"> """ + name + """</span>"""
	sidebarUnitButtonsContent += "</a>"
	sidebarUnitButtonsContent += """<span class="tooltip"> """ + name + """</span>"""
	sidebarUnitButtonsContent += "</li>\n"

sidebars = {
	'application': build_sidebar("index.html", websiteData['Global Class Name'], "overview_application.html", "Overview", "'bx bxs-shapes'", appButtonsContent,bool(False)),
	'outcome': build_sidebar("index.html", websiteData['Global Class Name'], "overview_outcome.html", "Overview", "'bx bxs-shapes'", outcomeButtonsContent, bool(False)),
	'unit': build_sidebar("courseInfo.html", websiteData['Course Offering Title'], "overview_calendar.html", "Calendar", "'bx bx-calendar'", sidebarUnitButtonsContent, bool(True)),
	'unitSecondary': secondaryUnitBoxes()
}

mobile_sidebars = {
	'application': build_mobile_sidebar("index.html", websiteData['Global Class Name'], "overview_application.html", "Overview", appMobileButtonsContent),
	'outcome': build_mobile_sidebar("index.html", websiteData['Global Class Name'], "overview_outcome.html", "Overview", outcomeMobileButtonsContent),
	'unit': build_mobile_sidebar("courseInfo.html", websiteData['Course Offering Title'], "overview_calendar.html", "Calendar", unitMobileButtonsContent),
}

head_html = {
	'application': build_head_html(websiteData['Global Class Name']),
	'outcome': build_head_html(websiteData['Global Class Name']),
	'unit': build_head_html(websiteData['Course Offering Title']),
	'others': build_head_html(websiteData['Global Class Name'])
}

def create_unit_boxes():
	#variables used in for loop

	boxString = ""
	# boxString = """<p><a href=\"supplemental_videos.html\"> Supplemental Videos </a></p>"""
	boxString += """ <button class="button coll" onclick="expandCollapseAll(0)">Expand All Boxes</button>
				<button class="button coll" onclick="expandCollapseAll(1)">Collapse All Boxes</button><br><br>"""
	
	# MIA Commented out for start of quarter
	# boxString += """<p>Compiled weeks file <a href="../output/lessons/complete-week.pdf" download>download</a></p>"""

	for i in range(len(unitData)):
		unitNumber = i+1
    	#set appropriate variables for top calendar information section and title 
		heading=unitData[i]['header']
		
		if('outcomes' in unitData[i]):
			heading+=": " + unitData[i]['outcomes']
		info=""
		if('CalendarInfo' in unitData[i]):
			info+=unitData[i]['CalendarInfo']
		
		#box heading and subheading/description
		if(unitData[i]['ExpandInCalendar']):
			boxString += """<div class="box" style="background-color: white;" id="box"""+str(unitNumber)+""""><button type="button" class="collapsible active" 
			style="background-color: white;"> \n"""
			boxString += """<h2 style= "line-height:20px;"> <i id="sideBtn"""+ str(unitNumber)+ """" class='bx bx-caret-down'></i> 
				""" + heading + "</h2> </button> "
			boxString += """<div class="boxContent" style="display: block;"> <p> """+ info + """</p>"""
		else:
			boxString += """<div class="box" style="background-color: lightgray;" id="box"""+str(unitNumber)+""""><button type="button" class="collapsible"
			style="background-color: lightgray;"> \n"""
			boxString += """<h2 style= "line-height:20px;"> <i id="sideBtn"""+ str(unitNumber)+ """" class='bx bx-caret-right'></i> 
				""" + heading + "</h2> </button> "
			boxString += """<div class="boxContent" style="display: none;"> <p> """+ info + """</p>"""
			
		boxString += "<hr>"
		
		#list begins
		#boxString += """<div class="column"> <dl> \n"""
		boxString += """<div><dl> \n"""
		#Learning Materials (link to contents on weekly page)
		boxString += """<dt>Learning Materials</dt><dd>"""		
		#pdfs
		if('content' in unitData[i]):
			for content in unitData[i]['content']:
				# print(content['name'])
				pdfjsID = content['name'].replace(" ", "-")
				boxString += "<a href=\"unit""" +str(unitNumber)+ """.html#"""+ pdfjsID+"""\" >""" + content['name'] + """</a>&emsp;"""				
		
		boxString += "</dd>"
    	#Assignments
		boxString += """<dt>Due Dates</dt> \n"""
		if ('Due Dates' in unitData[i]):
			for assignment in unitData[i]['Due Dates']:
				#if link is provided use that link
				link = "<a href=\""
				if('link' in assignment):
					link += assignment['link']
					link += "\">"+ assignment['name'] + "</a>"
            	#else refer to the assignments page (default)
				else:
					link +="assignments.html"
					link += "\" target=\"_blank\">"+ assignment['name'] + "</a>"
				#add due date of assignment based on unit_settings or, if not present, based on assignmentData
				assignmentDict = next((assnt for assnt in assignmentData if assnt["name"] == assignment['name']), False)
				due = ""
				if('due' in assignment):
					due+= "Due: "
					due+= assignment['due']
				elif(assignmentDict and 'due' in assignmentDict):
					due+= "Due: "
					due+= assignmentDict['due']
				boxString += "<dd>" + link + " <div class=\"badge due\">"+due+"</div> </dd>\n"
		
		boxString += "</dl></div></div>"
		
		boxString += "</div><br>"


	# print(boxString)
 	#collapsible script 
	boxString += """<script>
	var coll = document.getElementsByClassName("collapsible");
	var i;
	
	var boxNumber;
	var expanded; 
	url = window.location.href;

	queryString();

	function queryString(box){
		var qInd;
		var boxValue;
		var expandedValue;
		var valuesAdded = 0; 

		for( i=0; i<url.length; i++){
			if(url[i]==="="){
				valuesAdded++;
				i++; //go to value next to = 

				//boxNumber must always be before expanded, 
				// and both have one character values (0 or 1)
				if(valuesAdded == 1){
					boxValue = url[i]; 
				}
				else {
					expandedValue = url[i];
				}
				
				console.log("value: "+url[i]);
			}
		}
	}
	
	for (i = 0; i < coll.length; i++) {
		sideBtnString="#sideBtn";
		sideBtnString+=(i+1);
		boxString="#box";
		boxString +=(i+1);
		let sideBtn = document.querySelector(sideBtnString);
		let box = document.querySelector(boxString);
		let h2 = document.querySelector("h2");

  		coll[i].addEventListener("click", function() {
    		this.classList.toggle("active");
    		var content = this.nextElementSibling;
    	
			if (content.style.display === "block") {
      			content.style.display = "none";
				box.style.background = "lightgray";
				this.style.background = "lightgray";
				h2.style.lineHeight="20px";
    		} 
			else {
      			content.style.display = "block";
				box.style.background = "white";
				this.style.background = "white";
				h2.style.lineHeight="20px";
    		}
			if(this.classList.contains("active")){
				sideBtn.classList.replace("bx-caret-right", "bx-caret-down");//replacing the icons class
			}
			else {
			sideBtn.classList.replace("bx-caret-down","bx-caret-right");//replacing the icons class
			}
		});
	}

	function expandCollapseAll(bool, multiple) {
		var coll = document.getElementsByClassName("collapsible");
		var i;
		for (i = 0; i < coll.length; i++) {
			sideBtnString="#sideBtn";
			sideBtnString+=(i+1);
			boxString="#box";
			boxString +=(i+1);
			let sideBtn = document.querySelector(sideBtnString);
			let box = document.querySelector(boxString);

			//coll[i].classList.toggle("active");
    		var content = coll[i].nextElementSibling;

			if(bool==0){
				//expand all 
				content.style.display = "block";
				sideBtn.classList.replace("bx-caret-right", "bx-caret-down");//replacing the icons class
				coll[i].style.background= "white";
				box.style.background="white";
			}
			else{
				 //collapse all
				content.style.display = "none";
				sideBtn.classList.replace("bx-caret-down","bx-caret-right");//replacing the icons class
				coll[i].style.background= "lightgray";
				box.style.background="lightgray";
			}
		}

		return bool;
	}


	</script>"""
		
	return boxString

def create_outcome_boxes():
	boxString = ""
	childNum = 1
	#big for loop begin
	for i in outcomeData:

		boxString += """<div class="box"> \n"""

		boxString += "<h2>" + outcomeData[i]['Icon'] + i + "</h2>"
		boxString += "<p> Description: " + outcomeData[i]['Description'] + "</p>"
		boxString += "<hr>"

		boxString += """<div class="column"> <dl> \n"""

		
		for j in outcomeData[i]['Children']:

			#add link to page of 2nd tier children with suboutcomes (only link to pages of 2nd tier children with content)
			if(bool(outcomeData[i]['Children'][j]['Children'])):
				boxString += """<dt><i class='bx bx-subdirectory-right' ></i><a href=\"""" + outcomeData[i]['Children'][j]['file'] + """?box=1\" >""" + j + """</a></dt> \n"""
				
			else:
				boxString += """<dt><i class='bx bx-subdirectory-right' ></i><a href="javascript:void(0)" >""" + j + """</a></dt> \n"""
			

			#list children of 2nd tier children (suboutcomes under outcomes, these will be included on the webpage for the outcomes as PDFs and menu options)
			if(bool(outcomeData[i]['Children'][j]['Children'])):
				#reset counter
				childNum = 1 
				for k in outcomeData[i]['Children'][j]['Children']:
					kdesc = outcomeData[i]['Children'][j]['Children'][k]['Description']
					boxString += """<dd> <a href=\""""+outcomeData[i]['Children'][j]['file']+"""?box=""" +str(childNum)+"""\" >""" + kdesc + """</a> </dd>\n"""
					childNum+=1
				
				boxString += "</dl>"

		boxString += "</div>"

		boxString += "</div><br><br>"
	return boxString

def create_application_boxes():
	boxString = ""
	# boxString = """<div class="box"> \n"""
	#big for loop begin
	for i in appData:
		file = i.replace(" ", "-").lower()+".html"
		boxString += """<h2 style="line-height: 60px;"> <i class='bx bxs-chevron-right-square'></i> <a href= \"""" + file + """\" style="color: #182B49; text-decoration: none; font-weight: 500;" >""" + i + """</a></h2>\n"""
	# boxString += "</div><br><br>"
	return boxString

def create_copyright():
	copyright = """<div class="copyright">"""
	copyright += "Copyright © " + websiteData["Copyright Year"] + " " + websiteData["Copyright Name"] + "<br>"
	copyright += """<a style= "color:white;" href="feedback.html">Feedback</a></div>"""
	return copyright

def create_feedback():
	feedback = """<div class="feedback_form">""" + websiteData["Feedback"] + """</div>"""
	return feedback

def create_title():
	title = websiteData["Global Class Name"]
	return title

def create_course_offering_title():
	course_title = websiteData["Course Offering Title"]
	return course_title

def create_term():
	term = websiteData["Term"]
	return term

def create_assignment():
#	assignmentData = json.loads(open("assignments.json").read())  #available globally now
	templateString = ""
	
	collapseVar = 0
	#main for loop begin (only for collapsible menu items)
	for element in assignmentData:
		pdf=""
		tex=""
		html=""
		
		#increment collapseVar (helps with collapsible card menu function)
		collapseVar+= 1
		
		#format all filenames if addExtensions is true
		if(element['addExtensions']):
			pdf="../output/assignments/"+element['name']+".pdf"
			tex= zip_file(element['name'],"assignments-flat")

			if(not tex):
				tex = ""

			html="../output/assignments/"+element['name']+".html"
		else:
			pdf="../files/"+element['name']+".pdf"
			
		#heading and collapsible card stuff
		cardID = element['name'].replace(" ", "").lower()

		#format assignment name, as namme is just file name
		assignmentName= element['name'].replace("-", " ").title().replace("Cse20F21","")

		templateString += """<div class="box outcome"  id="box"""+str(collapseVar)+""""><button type="button" class="collapsible"
			"> \n"""
		templateString += """<h2 style= "line-height:20px;"> <i id="sideBtn"""+ str(collapseVar)+ """" class='bx bx-caret-right'></i> 
			""" + assignmentName + """</h2> </button> <div class="boxContent" style="display: none;"> <hr>"""
            

    	#Assignment Information
		templateString += """ <p> """+ element['Information']+"""</p>"""
		dueDate = ""; 
		for week in unitData:
			for assignment in week['Due Dates']:
				if element["name"] in assignment["name"]:
					if "due" in assignment:
						dueDate = assignment["due"]
						# print(element['name']+"\ndue: "+dueDate)

		templateString += """ <p> Due: """ + dueDate + """</p>"""
    	#.pdf Download button
		templateString += """ <p> <a tabindex = "2" class="button PDF" aria-label="Download PDF" 
		href="""+pdf+""" download>PDF</a>"""

    	#html and tex download buttons
		if(element['addExtensions']):
        	#.tex
			templateString += """ <a tabindex = "2" style= "display: inline-block;" class="button LaTeX" aria-label="Download .LaTeX" 
			href=""" + tex + """ download>LaTeX</a> """

        	#.html
			templateString += """ <a tabindex = "2" style= "display: inline-block;" class="button HTML" aria-label="Open HTML file of Document in New Tab" 
			href= """ + html + """ target="HTML">Raw HTML</a><br>"""
        
		#id of pdf.js element formatting
		pdfjsID = element['name'].replace(" ", "-")
    	
		#Solutions on/off buttons 
		if('solutionsFile' in element):
			templateString += """ <label>Sample solutions<input type="checkbox" id="toggle-""" + str(collapseVar) + """">
				<span class="slider round"></span>
				<script>
					annotated""" + str(collapseVar) + """ = false;
					document.getElementById("toggle-""" + str(collapseVar) + """").onclick = function() {
						if(annotated""" + str(collapseVar) + """  == false) {
							console.log("false to true");
							annotated""" + str(collapseVar) + """  = true;
							annotations(true, \""""+pdf+ """\",\"../files/"""+element['solutionsFile']+"""\", \"""" + pdfjsID + """\")
						}
						else {
							console.log("true to false");
							annotated""" + str(collapseVar) + """  = false;
							annotations(false, \""""+pdf+ """\",\"../files/"""+element['solutionsFile']+"""\", \"""" + pdfjsID + """\")
						}
					}

					
				</script></label>
			"""
        	
			
			# templateString += """ <a tabindex = "2" class="button on" aria-label="Solutions On" id="solutionsOnButton"""+str(collapseVar)+ """/" href="javascript:void(0)" >Solutions On</a>
			# <a tabindex = "2" class="button off" aria-label="Solutions Off" id="solutionsOffButton"""+str(collapseVar)+ """/" href="javascript:void(0)" >Solutions Off</a> """

       		# #solutions on
			# templateString += """ <script> document.getElementById("solutionsOnButton"""+str(collapseVar)+ """/").onclick = function() {annotations(1,
			# \""""+pdf+ """\",\"../files/"""+element['solutionsFile']+"""\", \""""+pdfjsID+ """\")};"""
            
        	# #solutions off
			# templateString +="""document.getElementById("solutionsOffButton"""+str(collapseVar)+ """/").onclick = function() {annotations(0,
			# \""""+pdf+ """\",\"../files/"""+element['solutionsFile']+"""\", \""""+pdfjsID+ """\")};
			# </script>"""
            
    	#pdf.js embed 
		templateString += """ <br> <iframe class="PDFjs" id=\""""+ pdfjsID +"""\" src="web/viewer.html?file=../"""+ pdf+ """" 
		title="webviewer" frameborder="0" width="100%" height="600"></iframe> """
		#script for solutions 
		templateString += """<script>
			 toggle = document.querySelector('.toggle input')

			toggle.addEventListener('click', () => {
    		 onOff = toggle.parentNode.querySelector('.onoff"""+str(collapseVar)+"""')
    		onOff.textContent = toggle.checked ? 'ON' : 'OFF'
			})
			
			function annotations(notes, annotated,id) {
				var doc;
				var drive;
				 toggle = document.querySelector('.toggle input')
				//0 value means annotations are off 
				if (toggle.checked) {
					doc = "web/viewer.html?file=../"+notes
				} 

				//1 value turns annotations on
				else {
					doc = "web/viewer.html?file=../" +annotated
				}
				
                document.getElementById(id).src = doc;
			}
		</script>"""
    	#closing div for collapsible menu item 
		templateString += """</div></div>"""
            
      	

	templateString += """<script>
	var coll = document.getElementsByClassName("collapsible");
	var i;
	
	var boxNumber;
	var expanded; 
	url = window.location.href;

	queryString();

	function queryString(box){
		var qInd;
		var boxValue;
		var expandedValue;
		var valuesAdded = 0; 

		for( i=0; i<url.length; i++){
			if(url[i]==="="){
				valuesAdded++;
				i++; //go to value next to = 

				//boxNumber must always be before expanded, 
				// and both have one character values (0 or 1)
				if(valuesAdded == 1){
					boxValue = url[i]; 
				}
				else {
					expandedValue = url[i];
				}
				
				console.log("value: "+url[i]);
			}
		}
	}
	
	for (i = 0; i < coll.length; i++) {
		sideBtnString="#sideBtn";
		sideBtnString+=(i+1);
		boxString="#box";
		boxString +=(i+1);
		console.log(boxString);
		let sideBtn = document.querySelector(sideBtnString);
		let box = document.querySelector(boxString);
		let h2 = document.querySelector("h2");

  		coll[i].addEventListener("click", function() {
    		this.classList.toggle("active");
    		var content = this.nextElementSibling;
    	
			if (content.style.display === "block") {
      			content.style.display = "none";
				h2.style.lineHeight="20px";
    		} 
			else {
      			content.style.display = "block";
				h2.style.lineHeight="20px";
    		}
			if(this.classList.contains("active")){
				sideBtn.classList.replace("bx-caret-right", "bx-caret-down");//replacing the icons class
			}
			else {
			sideBtn.classList.replace("bx-caret-down","bx-caret-right");//replacing the icons class
			}
		});
	}

	function expandCollapseAll(bool, multiple) {
		var coll = document.getElementsByClassName("collapsible");
		var i;
		for (i = 0; i < coll.length; i++) {
			sideBtnString="#sideBtn";
			sideBtnString+=(i+1);
			boxString="#box";
			boxString +=(i+1);
			let sideBtn = document.querySelector(sideBtnString);
			let box = document.querySelector(boxString);

			//coll[i].classList.toggle("active");
    		var content = coll[i].nextElementSibling;

			if(bool==0){
				//expand all 
				content.style.display = "block";
				sideBtn.classList.replace("bx-caret-right", "bx-caret-down");//replacing the icons class
				coll[i].style.background= "white";
				box.style.background="white";
			}
			else{
				 //collapse all
				content.style.display = "none";
				sideBtn.classList.replace("bx-caret-down","bx-caret-right");//replacing the icons class
				coll[i].style.background= "lightgray";
				box.style.background="lightgray";
			}
		}

		return bool;
	}


	</script>"""
		
	return templateString

def substitute_template(input, output):
	templateOpener = open("templates/" + input + ".html", "r")
	templateString = Template(templateOpener.read())
	
	page_variables = site_variables.copy()
	page_variables.update(dict())
    
    # Substitute settings unitData with appropriate variables 
	result = templateString.substitute(page_variables)

	write_if_different("generated/website/" + output + ".html", result)
    
    # Close files
	templateOpener.close()

def create_office_hours():
	officehours = websiteData['Office Hours']
	return officehours

def create_full_definition():
	full_definition = websiteData['Compiled Activity Snippets']
	fullDefinition = ""
	
	if(full_definition == "True"):
		fullDefinition = """<p>Compiled defintions file <a href="../output/activity-snippets/full-definition.pdf" download>download</a></p>"""
	
	return fullDefinition


def create_compiled_assignments():
	compiled = websiteData['Compiled Assignments']
	text = ""
	
	if(compiled == "True"):
		text = """<p>Compiled assignments file <a href="../output/assignments/assignments-compiled.pdf" download>download</a></p>"""

	return text
def write_if_different(filename, contents):
    try:
        old_contents = open(filename).read()
        if old_contents == contents: return
    except FileNotFoundError:
        pass # If the file doesn't exist, continue so we can create it!
    result_file = open(filename, "w")
    result_file.write(contents)
    result_file.close()

def create_site_variables():
	return {
		'applicationSidebar': sidebars['application'],
		'outcomeSidebar': sidebars['outcome'],
		'unitSidebar': sidebars['unit'],
		'unitSecondarySidebar': sidebars['unitSecondary'],

		'applicationMobileSidebar': mobile_sidebars['application'],
		'outcomeMobileSidebar': mobile_sidebars['outcome'],
		'unitMobileSidebar': mobile_sidebars['unit'],

		'applicationHead': head_html['application'],
		'outcomeHead': head_html['outcome'],
		'unitHead': head_html['unit'],
		'othersHead': head_html['others'],

		'unitBoxes': create_unit_boxes(),
		'outcomeBoxes': create_outcome_boxes(),
		'applicationBoxes': create_application_boxes(),
		'fullDefinition': create_full_definition(),
		'compiledAssignments': create_compiled_assignments(),

		'copyrightFooter': create_copyright(),
		'feedbackForm': create_feedback(),
		'mainTitle': create_title(),
		'courseTitle': create_course_offering_title(),
		'Term': create_term(),
		'collapsibleMenu': create_assignment(),
		'officehourslink': create_office_hours()
	}

site_variables = create_site_variables()