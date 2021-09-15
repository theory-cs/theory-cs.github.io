from string import Template
import json


websiteData = json.loads(open("website-settings.json").read())


def sidebar(view):

    view = view.lower()

	hrefApplication = "overviewApplication.html"
	overviewApplication= """<li>
		<a href="overviewApplication.html" aria-label="Go to Overview">
		<i class='bx bxs-shapes'></i>
		<span class="links_name">Overview</span>
		</a>
		<span class="tooltip">Overview</span>
		</li>"""

    sidebarTop = """<div class="sidebar">
		<div class="logo-details">
		<div class="logo_name">
		<i class='bx bx-home-smile'>
		</i> </div> """

	sidebarButtons = "" 
    
    if("application" in view):
        appData = json.loads(open("applications.json").read())
        sidebarButtons += """ <a href="index.html" class="logo_name">""" + websiteData['Global Class Name']+ """</a> <!--NAME-->
			<i class='bx bx-chevron-right' id="btn" ></i>
		</div>

		<ul class="nav-list">
			
			<li>
				<a href="overviewApplication.html" aria-label="Go to Overview">
					<i class='bx bxs-shapes'></i>
					<span class="links_name">Overview</span>
				</a>
				<span class="tooltip">Overview</span>
			</li>"""

        for i in appData:
            file = i.replace(" ", "-").lower()+".html"
            sidebarButtons += "<li>"
            sidebarButtons += """<a href= \"""" + file + """\" aria-label="Go to """ + i + """ ">"""
            sidebarButtons += """<i><p class="icons">&nbsp;&nbsp;""" + appData[i]['Icon'] + """</p></i>"""
            sidebarButtons += """<span class="links_name"> """ + i + """</span>"""
            sidebarButtons += "</a>"
            sidebarButtons += """<span class="tooltip"> """ + i + """</span>"""
            sidebarButtons += "</li>\n"


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
    
    elif("topic" in view):
        outcomeData = json.loads(open("outcomes.json").read())
        sidebarButtons += """<a href="index.html" class="logo_name">""" + websiteData['Global Class Name']+"""</a>
			<i class='bx bx-chevron-right' id="btn" ></i>
		        </div>

		        <ul class="nav-list">
    
            <li>
				<a href="overviewTopic.html" aria-label="Go to Overview">
					<i class='bx bxs-shapes'></i>
					<span class="links_name">Overview</span>
				</a>
				<span class="tooltip">Overview</span>
			</li>"""
        
        for big in outcomeData:
            for med in outcomeData[big]['Children']:
            #only put icon in sidebar of 2nd tier topics that have children 
                if(bool(outcomeData[big]['Children'][med]['Children'])):
                    sidebarButtons += "<li>"
                    sidebarButtons += """<a href= \"""" +outcomeData[big]['Children'][med]['file'] + """\" aria-label="Go to """ + med + """ ">"""
                    sidebarButtons += """<i><p class="icons">&nbsp;&nbsp;""" + outcomeData[big]['Children'][med]['Icon'] + """</p></i>"""
                    sidebarButtons += """<span class="links_name"> """ + med + """</span>"""
                    sidebarButtons += "</a>"
                    sidebarButtons += """<span class="tooltip"> """ + med + """</span>"""
                    sidebarButtons += "</li>"

        #end div tags and script for sidebar
        sidebarButtons += """</ul>
	        </div> 
		
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
	        </script>		"""
    
    elif("unit" in view):
        unitData = json.loads(open("unit-settings.json").read())
        sidebarButtons += """ <a href="overviewCalendar.html" class="logo_name">""" + websiteData['Course Offering Title']+"""</a> <!--NAME-->
			<i class='bx bx-chevron-right' id="btn" ></i>
		</div>

		<ul class="nav-list">
			
			<li>
				<a href="overviewCalendar.html" aria-label="Go to Calendar">
					<i class='bx bx-calendar'></i>
					<span class="links_name">Calendar</span>
				</a>
				<span class="tooltip">Calendar</span>
			</li>"""
        

        for i in range(0,len(unitData)):
            sidebarButtons += "<li>"
            sidebarButtons += """<a href= " """ + 'unit'+str(i+1) + """.html" aria-label="Go to """ + unitData[i]['header'] + """ ">"""
            sidebarButtons += """<i><p class="icons">&nbsp;&nbsp;&nbsp;&nbsp;""" + str(i+1) + """</p></i>"""
            sidebarButtons += """<span class="links_name"> """ + unitData[i]['header'] + """</span>"""
            sidebarButtons += "</a>"
            sidebarButtons += """<span class="tooltip"> """ + unitData[i]['header'] + """</span>"""
            sidebarButtons += "</li>"


        sidebarButtons += """ </ul>
		    </div>
		
        
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
		   }else {
			 closeBtn.classList.replace("bx-chevron-left","bx-chevron-right");//replacing the iocns class
		   }
		  }
		</script>
        """
    
    return sidebarButtons



    