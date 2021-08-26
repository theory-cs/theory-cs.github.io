all: $(patsubst notes/%.tex,output/%.pdf,$(wildcard notes/*.tex))

generated: generated-output generated-annotatedNotes generated-notes generated-resources generated-website generated-website-css generated-notes-Activity-Snippets 

website: generated python pandoc

generated-output: all $(patsubst output/%.pdf,generated/output/%.pdf,$(patsubst notes/%.tex,output/%.pdf,$(wildcard notes/*.tex)))
generated-build: $(patsubst build/%,generated/build/%,$(wildcard build/*))
generated-annotatedNotes: $(patsubst annotatedNotes/%,generated/annotatedNotes/%,$(wildcard annotatedNotes/*))
generated-notes: $(patsubst notes/%,generated/notes/%,$(wildcard notes/*))
generated-resources: $(patsubst resources/%,generated/resources/%,$(wildcard resources/*))
generated-website: $(patsubst website/%,generated/website/%,$(wildcard website/*))
generated-website-css:  $(patsubst website/css/%,generated/website/css/%,$(wildcard website/css/*))
generated-notes-Activity-Snippets: $(patsubst notes/Activity-Snippets/%,generated/notes/Activity-Snippets/%,$(wildcard notes/Activity-Snippets/*))

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

generated/notes/Activity-Snippets/%: notes/Activity-Snippets/%
	mkdir -p generated/notes/Activity-Snippets
	cp $< $@

generated/annotatedNotes/%.pdf: annotatedNotes/%.pdf
	mkdir -p generated/annotatedNotes
	cp $< $@

# NOTE(joe): an assumption! output only contains PDFs as interesting content to
# copy. Need to generalize to more extensions if we want that!
generated/output/%: output/%
	mkdir -p generated/output
	cp $< $@


output/%.pdf: notes/%.tex resources/CSE20packages.tex
	mkdir -p output; cd notes; pdflatex -output-directory ../output $(<F) 

clean: 
	cd output; rm *.out *.log *.aux

python: 
	python3 unitTemplate.py

pandoc:
	cd notes/Lessons
	pandoc --standalone --mathjax -f latex -t html *.tex -o ../../generated/website/*.html


