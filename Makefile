# To build website, first create PDFs and static elements in generated directory, then
# translate tex to htmls and then dynamically create additional html pages
# and finally remove auxiliary files from typesetting steps
website: generated pandoc python clean

#website: copy-files generated-notes generated-resources generated-website generated-website-css generated-notes-activity-snippets 
#copy-files: generated-output generated-annotated-notes

generated: generated-output generated-files generated-notes generated-resources generated-website generated-website-css generated-notes-activity-snippets 

# Typesetting all .tex files in notes/lessons directory
output/%.pdf: notes/lessons/%.tex resources/lesson-head.tex resources/discrete-math-packages.tex
	mkdir -p output; cd notes; cd lessons; pdflatex -output-directory ../../output $(<F) 

# Removing all auxiliary files from output directory
clean: 
	cd output; rm -f *.out *.log *.aux

# Building dynamic html pages based on unit template (TODO: also build pages for topics and outcomes)
python: 
	python3 unitTemplate.py
	python3 topicTemplate.py

#Building html versions of all .tex files in notes/lessons directory (TODO: also need for topics and outcomes)
output/%.html: notes/lessons/%.tex resources/lesson-head.tex resources/discrete-math-packages.tex
	cd notes/lessons; pandoc --standalone --mathjax -f latex -t html $(<F) -o ../../output/$(@F)

# (Mia) I don't understand these yet

# Target files are all pdfs in output
all: $(patsubst notes/Lessons/%.tex,output/%.pdf,$(wildcard notes/Lessons/*.tex))

# First do target all, then do targets that look like generated/output/SOMETHING.pdf
generated-output: all $(patsubst output/%.pdf,generated/output/%.pdf,$(patsubst notes/Lessons/%.tex,output/%.pdf,$(wildcard notes/Lessons/*.tex)))


generated-build: $(patsubst build/%,generated/build/%,$(wildcard build/*))
generated-files: $(patsubst files/%,generated/files/%,$(wildcard files/*))
generated-notes: $(patsubst notes/%,generated/notes/%,$(wildcard notes/*))
generated-resources: $(patsubst resources/%,generated/resources/%,$(wildcard resources/*))
generated-website: $(patsubst website/%,generated/website/%,$(wildcard website/*))
generated-website-css:  $(patsubst website/css/%,generated/website/css/%,$(wildcard website/css/*))
generated-notes-activity-snippets: $(patsubst notes/activity-snippets/%,generated/notes/activity-snippets/%,$(wildcard notes/activity-snippets/*))
pandoc : $(patsubst output/%.html,generated/output/%.html,$(patsubst notes/lessons/%.tex,output/%.html,$(wildcard notes/lessons/*.tex)))

generated/website/%: website/%
	mkdir -p generated/website
	cp -R $< $@

generated/website/css/%: website/css/%
	mkdir -p generated/website/css
	cp $< $@

generated/resources/%: resources/%
	mkdir -p generated/resources
	cp -R $< $@

generated/notes/%: notes/%
	mkdir -p generated/notes
	cp -R $< $@

generated/notes/activity-snippets/%: notes/activity-snippets/%
	mkdir -p generated/notes/activity-snippets
	cp $< $@

generated/files/%.pdf: files/%.pdf
	mkdir -p generated/files
	cp $< $@

# NOTE(joe): an assumption! output only contains PDFs as interesting content to
# copy. Need to generalize to more extensions if we want that!
generated/output/%: output/%
	mkdir -p generated/output
	cp $< $@
