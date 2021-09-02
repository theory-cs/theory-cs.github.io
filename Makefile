# The files that drive website changes are the tex files for lessons.
# To build the website, first create PDFs and static elements in generated directory, then
# translate tex to htmls and then dynamically create additional html pages
# and finally remove auxiliary files from typesetting steps
website: latex static-pages dynamic-pages tex-html clean-tex

# Iterate over all changed .tex files in notes/lessons and run target for them in new folder
latex: $(patsubst notes/lessons/%.tex,generated/output/%.pdf,$(wildcard notes/lessons/*.tex))

# Typesetting all .tex files in notes/lessons directory
generated/output/%.pdf: notes/lessons/%.tex resources/lesson-head.tex resources/discrete-math-packages.tex
	mkdir -p generated/output; cd notes; cd lessons; pdflatex -output-directory ../../generated/output $(<F) 


# Build website by copying over files, notes, resources, html, and style files to generated directory
static-pages: generated-files generated-resources generated-notes  generated-notes-activity-snippets generated-website generated-website-temp generated-website-css

# Directory files has instructor-added content, e.g. annotated pdfs and slides
generated-files: $(patsubst files/%,generated/files/%,$(wildcard files/*))

generated/files/%: files/%
	mkdir -p generated/files
	cp $< $@

# Directory resources has images and tex files used to create lessons
# TODO: consider only copying image files once all .tex files that are presented to public-facing
# website are flattened to remove \input of lesson-head and discrete-math-packages
generated-resources: $(patsubst resources/%,generated/resources/%,$(wildcard resources/*))

generated/resources/%: resources/%
	mkdir -p generated/resources
	cp -R $< $@

# Directory notes contains tex files for outcomes and topics 
# TODO: remove this once the tex files are created by a script that scrapes tags from lessons
generated-notes: $(patsubst notes/%,generated/notes/%,$(wildcard notes/*))

generated/notes/%: notes/%
	mkdir -p generated/notes
	cp -R $< $@

# Directory notes/activity-snippets contains tex files for outcomes and topics 
# TODO: remove this once the tex files are created by a script that scrapes tags from lessons
generated-notes-activity-snippets: $(patsubst notes/activity-snippets/%,generated/notes/activity-snippets/%,$(wildcard notes/activity-snippets/*))

generated/notes/activity-snippets/%: notes/activity-snippets/%
	mkdir -p generated/notes/activity-snippets
	cp $< $@

# Directory website  and website-manual-to-automate contain all static components of site
# TODO: edit these components to use dynamic sidebar
generated-website: $(patsubst website/%,generated/website/%,$(wildcard website/*))

generated/website/%: website/%
	mkdir -p generated/website
	cp -R $< $@

# Directory website-manual-to-automate contains placeholder versions of pages that will be 
# created by appTemplate.py and outcomes-list.py  TODO: remove once automated versions exist
generated-website-temp: $(patsubst website-manual-to-automate/%,generated/website/%,$(wildcard website-manual-to-automate/*))

generated/website/%: website-manual-to-automate/%
	mkdir -p generated/website
	cp -R $< $@

# Directory website/css contains styling information that may change when pages are updated, 
# for example, the contents of the sidebar depend on the number of lessons, outcomes, and applications
generated-website-css:  $(patsubst website/css/%,generated/website/css/%,$(wildcard website/css/*))

generated/website/css/%: website/css/%
	mkdir -p generated/website/css
	cp $< $@

# Building dynamic html pages based on unit template, topic (TODO: rename as outcome) template
# application template, and overview pages. These dynamic html pages are created
# directly in the generated directory
dynamic-pages: 
	python3 unitTemplate.py
	python3 topicTemplate.py
	python3 appTemplate.py
	python3 overviewTopicTemplate.py

#Building html versions of all .tex files in notes/lessons directory 
#TODO: also need for topics and outcomes, potentially as part of python scripts creating them
tex-html : $(patsubst generated/output/%.html,generated/output/%.html,$(patsubst notes/lessons/%.tex,generated/output/%.html,$(wildcard notes/lessons/*.tex)))

generated/output/%.html: notes/lessons/%.tex resources/lesson-head.tex resources/discrete-math-packages.tex
	cd notes/lessons; pandoc --standalone --mathjax -f latex -t html $(<F) -o ../../generated/output/$(@F)

# Removing all auxiliary typesetting files from output directory
clean-tex: 
	cd generated/output; rm -f *.out *.log *.aux
