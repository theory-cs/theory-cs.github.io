from string import Template
import json
from user_functions import *
from create_zip import *

# Opening JSON file
outcomeData = json.loads(open("outcomes.json").read())

#main for loop begin
for big in outcomeData:
	for med in outcomeData[big]['Children']:
		pdfString = ""
		collapseVar = 1
		for small in outcomeData[big]['Children'][med]['Children']:
			tex= zip_file(file, "outcome-flat")
			if(tex == None):
				tex=""
			
			file = small.replace(" ", "-").lower()
			pdf="../output/outcome/" + file + ".pdf"
			html="../output/outcome/" + file + ".html"
			
			pdfString += """<div class="box outcome"  id="box"""+str(collapseVar)+""""><button type="button" class="collapsible"
			"> \n"""
			pdfString += """<h2 style= "line-height:20px;"> <i id="sideBtn"""+ str(collapseVar)+ """" class='bx bx-caret-right'></i> 
			""" + small + """</h2> </button> <div class="boxContent" style="display: none;"> <hr>"""
            
      		#Learning Goal
			pdfString += """ <p> Learning Goal: """+ outcomeData[big]['Children'][med]['Children'][small]['Description']+"""</p>"""
            
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
			pdfString += """ <br> <iframe class="PDFjs" id=\""""+ small +"""\" src="web/viewer.html?file=../"""+ pdf+ """" 
      		title="webviewer" frameborder="0" width="100%" height="600"></iframe> """

      		#closing div for collapsible menu item 
			pdfString += """</div></div>"""
            
      		#increment collapseVar
			collapseVar += 1

		pdfString += """<script>
		
			var coll = document.getElementsByClassName("collapsible");
	  		var i;
	
	  		var boxValue;
	  		url = window.location.href;
	  		var qInd;
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
				
			}
			}
	
			//debug
			console.log("boxValue: "+boxValue);
	
			//open certain box based on query string values 
			selectBox = "#box"+boxValue;
			let sBox = document.querySelector(selectBox);
			selectSideBtn= "#sideBtn"+boxValue;
			let sSideBtn = document.querySelector(selectSideBtn);

			coll[boxValue-1].style.background= "white";
			sBox.style.background="white";
			var content = coll[boxValue-1].nextElementSibling;
			content.style.display = "block";
			sSideBtn.classList.replace("bx-caret-right", "bx-caret-down");//replacing the icons class
	
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
		#Information Section
		infoString = "<p>"+ outcomeData[big]['Children'][med]['Description']+ "</p>" 
    
    
    	#open outcome_template html file and read it into a string 
		outcome_template = open("templates/outcome_template.html", "r")
		templateString = Template(outcome_template.read())

		page_variables = site_variables.copy()
		page_variables.update(dict(
    	heading = med,
    	Information = infoString, 
    	collapsibleMenu = pdfString
    	))

    	#substitute settings outcomeData with appropriate variables 
		result = templateString.substitute(page_variables)
	
		write_if_different("generated/website/"+outcomeData[big]['Children'][med]['file'], result)

#end for loop

# Closing files
outcome_template.close()
