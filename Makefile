all: $(patsubst notes/lessons/%.tex,output/%.pdf,$(wildcard notes/lessons/*.tex))

generated: generated-output generated-annotated-notes generated-notes generated-resources generated-website generated-website-css generated-notes-activity-snippets 

website: generated pandoc python

generated-output: all $(patsubst output/%.pdf,generated/output/%.pdf,$(patsubst notes/%.tex,output/%.pdf,$(wildcard notes/*.tex)))
generated-build: $(patsubst build/%,generated/build/%,$(wildcard build/*))
generated-annotated-notes: $(patsubst annotated-notes/%,generated/annotated-notes/%,$(wildcard annotated-notes/*))
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

generated/annotated-notes/%.pdf: annotated-notes/%.pdf
	mkdir -p generated/annotated-notes
	cp $< $@

# NOTE(joe): an assumption! output only contains PDFs as interesting content to
# copy. Need to generalize to more extensions if we want that!
generated/output/%: output/%
	mkdir -p generated/output
	cp $< $@


output/%.pdf: notes/%.tex resources/discrete-math-packages.tex
	mkdir -p output; cd notes; pdflatex -output-directory ../output $(<F) 

# NOTE(mia): adding typesetting step for lessons
output/%.pdf: notes/lessons/%.tex resources/lesson-head.tex
	mkdir -p output; cd Notes; cd Lessons; pdflatex -output-directory ../../output $(<F) 

clean: 
	cd output; rm *.out *.log *.aux

python: 
	python3 unitTemplate.py

output/%.html: notes/lessons/%.tex
	cd notes/lessons; pandoc --standalone --mathjax -f latex -t html $(<F) -o ../../output/$(@F)


