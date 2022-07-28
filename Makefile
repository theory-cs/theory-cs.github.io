usage:
	@echo 'Welcome to the build system for discrete-math-for-cs!'
	@echo 'You are seeing this message because you ran plain `make` or `make usage`'
	@echo 'The most common use of this Makefile is `make index; make website`'
	@echo 'This will populate the site, which you can navigate through `generated/website/index.html`'
	@echo 'You can read more about how to edit and build in README.md'

# This is named "index" because it does the aggregation and creation of files
# that don't have a one-to-one corresponding source file. This includes all the
# outcome and app files. Since getting `make` to understand intermediate generated
# files adds significant complexity, it's more straightforward to run two make
# commands in a row. The `website` rule relies on files created from *data* in
# the json files that index uses, so it needs to run in a totally separate step.
# The `index` rule sets this up.
index: generated/last-index.txt

# The files that drive website changes are the tex files for lessons.
# To build the website, first create PDFs and static elements in generated directory, then
# translate tex to htmls and then dynamically create additional html pages
# and finally remove auxiliary files from typesetting steps
website: static-pages latex dynamic-pages tex-html clean-tex 

# run compile python scripts to generated compiled .tex files of applications
# and outcomes. The target is a text file, and the trick of using touch makes the
# file update its modified time when this is run. BUT, if these files haven't
# changed since the last run, they will all be older than last-index.txt
generated/last-index.txt: *.json *.py notes/lessons/*.tex notes/assignments/*.tex notes/activity-snippets/*.tex resources/*.tex
	mkdir -p generated/notes
	mkdir -p generated/notes/app
	mkdir -p generated/notes/outcome
	mkdir -p generated/notes/activity-snippets-flat
	python3 weekly_compile_app.py
	python3 weekly_compile_outcome.py
	python3 assignments_compiled.py
	touch generated/last-index.txt


# Iterate over all changed .tex files in notes and run target for them in new folder, then generate flat versions if needed
latex: lessonsLatex appLatex outcomeLatex assignmentsLatex activitySnippetsLatex lessons-latexpand app-latexpand outcome-latexpand assignments-latexpand
lessonsLatex: $(patsubst notes/lessons/%.tex,generated/output/lessons/%.pdf,$(wildcard notes/lessons/*.tex))
appLatex: $(patsubst generated/notes/app/%.tex,generated/output/app/%.pdf,$(wildcard generated/notes/app/*.tex))
outcomeLatex: $(patsubst generated/notes/outcome/%.tex,generated/output/outcome/%.pdf,$(wildcard generated/notes/outcome/*.tex))
assignmentsLatex: $(patsubst notes/assignments/%.tex,generated/output/assignments/%.pdf,$(wildcard notes/assignments/*.tex))
activitySnippetsLatex: $(patsubst generated/notes/activity-snippets-flat/%.tex,generated/output/activity-snippets/%.pdf,$(wildcard generated/notes/activity-snippets-flat/*.tex))
outcome-latexpand: $(patsubst generated/notes/outcome/%.tex,generated/notes/outcome-flat/%.tex,$(wildcard generated/notes/outcome/*.tex))
app-latexpand: $(patsubst generated/notes/app/%.tex,generated/notes/app-flat/%.tex,$(wildcard generated/notes/app/*.tex))
lessons-latexpand: $(patsubst notes/lessons/%.tex,generated/notes/lessons-flat/%.tex,$(wildcard notes/lessons/*.tex))
assignments-latexpand: $(patsubst notes/assignments/%.tex,generated/notes/assignments-flat/%.tex,$(wildcard notes/assignments/*.tex))

# Typesetting all .tex files in notes/lessons directory MIA:added dependency on activity-snippets
generated/output/lessons/%.pdf: notes/lessons/%.tex notes/activity-snippets/*.tex resources/lesson-head.tex resources/discrete-math-packages.tex
	mkdir -p generated/output/lessons; cd notes/lessons; pdflatex -output-directory ../../generated/output/lessons $(<F) 

#since all of the app and outcome files are generated through a python script, they are in the generated directory 
# Typesetting all .tex files in generated/notes/app directory
generated/output/app/%.pdf: generated/notes/app/%.tex resources/lesson-head.tex resources/discrete-math-packages.tex
	mkdir -p generated/output/app; cd generated/notes/app; pdflatex -output-directory ../../output/app $(<F) 

# Typesetting all .tex files in generated/notes/app directory
generated/output/outcome/%.pdf: generated/notes/outcome/%.tex resources/lesson-head.tex resources/discrete-math-packages.tex
	mkdir -p generated/output/outcome; cd generated/notes/outcome; pdflatex -output-directory ../../output/outcome $(<F) 

# Typesetting all .tex files in notes/assignments directory
generated/output/assignments/%.pdf: notes/assignments/%.tex resources/assignment-head.tex resources/discrete-math-packages.tex
	mkdir -p generated/output/assignments; cd notes/assignments; pdflatex -output-directory ../../generated/output/assignments $(<F) 


# Typesetting all .tex files in generated/notes/activity-snippets-flat directory
generated/output/activity-snippets/%.pdf: generated/notes/activity-snippets-flat/%.tex resources/assignment-head.tex resources/discrete-math-packages.tex
	mkdir -p generated/output/activity-snippets; cd generated/notes/activity-snippets-flat; pdflatex -output-directory ../../output/activity-snippets $(<F) 

# generate expanded/flat version of assignments compiled tex files
generated/notes/assignments-flat/%.tex: notes/assignments/%.tex resources/assignment-head.tex resources/discrete-math-packages.tex
	mkdir -p generated/notes/assignments-flat; cd notes/assignments; latexpand $(<F) > ../../generated/notes/assignments-flat/$(<F)

# generate expanded/flat version of outcome compiled tex files
generated/notes/outcome-flat/%.tex: generated/notes/outcome/%.tex resources/lesson-head.tex resources/discrete-math-packages.tex
	mkdir -p generated/notes/outcome-flat; cd generated/notes/outcome; latexpand $(<F) > ../outcome-flat/$(<F)

# generate expanded/flat version of app compiled tex files
generated/notes/app-flat/%.tex: generated/notes/app/%.tex resources/lesson-head.tex resources/discrete-math-packages.tex
	mkdir -p generated/notes/app-flat; cd generated/notes/app; latexpand $(<F) > ../app-flat/$(<F)

# generate expanded/flat version of lessons compiled tex files
generated/notes/lessons-flat/%.tex: notes/lessons/%.tex resources/lesson-head.tex resources/discrete-math-packages.tex 
	mkdir -p generated/notes/lessons-flat; cd generated/notes/lessons; latexpand $(<F) > ../lessons-flat/$(<F)

# Build website by copying over files, notes, resources, html, and style files to generated directory
static-pages: generated-files generated-resources generated-notes generated-website 

# Directory files has instructor-added content, e.g. annotated pdfs and slides
generated-files: $(patsubst files/%,generated/files/%,$(wildcard files/*))

generated/files/%: files/% ./files/*/*
	mkdir -p generated/files
	cp -R $< $@

# Directory resources has images and tex files used to create lessons
generated-resources: $(patsubst resources/%,generated/resources/%,$(wildcard resources/*))

generated/resources/%: resources/% ./resources/*/*
	mkdir -p generated/resources
	cp -R $< $@

# Directory notes contains tex files for assignments, lessons, and activity snippets
generated-notes: $(patsubst notes/%,generated/notes/%,$(wildcard notes/*))

generated/notes/%: notes/% ./notes/*/*
	mkdir -p $@
	cp -R $</ $@

# Directory notes/activity-snippets contains tex files for outcomes and outcomes 
 generated-notes-activity-snippets: $(patsubst notes/activity-snippets/%,generated/notes/activity-snippets/%,$(wildcard notes/activity-snippets/*))

# generated/notes/activity-snippets/%: notes/activity-snippets/%
# 	mkdir -p generated/notes/activity-snippets
# 	cp $< $@

# Directory website and website-manual-to-automate contain all static components of site
generated-website: $(patsubst website/%,generated/website/%,$(wildcard website/*)) $(patsubst custom-html/%,generated/website/%,$(wildcard custom-html/*))

generated/website/%: website/% website/*/* website/* 
	mkdir -p $@
	cp -R $</ $@

generated/website/%: custom-html/% 
	cp $< $@

# Directory website/css contains styling information that may change when pages are updated, 
# for example, the contents of the sidebar depend on the number of lessons, outcomes, and applications
# generated-website-css:  $(patsubst website/css/%,generated/website/css/%,$(wildcard website/css/*))

# generated/website/css/%: website/css/%
# 	mkdir -p generated/website/css
# 	cp $< $@

# Building dynamic html pages based on unit template, outcome template
# application template, and overview pages. These dynamic html pages are created
# directly in the generated directory
dynamic-pages: 
	python3 template.py
	python3 unit_template.py
	python3 outcome_template.py
	python3 app_template.py
	python3 glossary.py
	python3 sitemap.py
	python3 supplemental_videos.py
	python3 activity_newtex.py
	python3 big_pdf_weekly_notes.py

#Building html versions of all .tex files in notes/lessons directory 
tex-html : lessons-tex-html app-tex-html outcome-tex-html assignments-tex-html activity-snippets-tex-html
lessons-tex-html : $(patsubst notes/lessons/%.tex,generated/output/lessons/%.html,$(wildcard notes/lessons/*.tex))
app-tex-html : $(patsubst generated/notes/app/%.tex,generated/output/app/%.html,$(wildcard generated/notes/app/*.tex))
outcome-tex-html : $(patsubst generated/notes/outcome/%.tex,generated/output/outcome/%.html,$(wildcard generated/notes/outcome/*.tex))
assignments-tex-html : $(patsubst notes/assignments/%.tex,generated/output/assignments/%.html,$(wildcard notes/assignments/*.tex))
activity-snippets-tex-html: $(patsubst generated/notes/activity-snippets-flat/%.tex,generated/output/activity-snippets/%.html,$(wildcard generated/notes/activity-snippets-flat/*.tex))

generated/output/lessons/%.html: notes/lessons/%.tex resources/lesson-head.tex resources/discrete-math-packages.tex
	cd notes/lessons; pandoc --standalone --mathjax -f latex -t html $(<F) -o ../../generated/output/lessons/$(@F)

generated/output/app/%.html: generated/notes/app/%.tex resources/lesson-head.tex resources/discrete-math-packages.tex
	cd generated/notes/app; pandoc --standalone --mathjax -f latex -t html $(<F) -o ../../output/app/$(@F)

generated/output/outcome/%.html: generated/notes/outcome/%.tex resources/lesson-head.tex resources/discrete-math-packages.tex
	cd generated/notes/outcome; pandoc --standalone --mathjax -f latex -t html $(<F) -o ../../output/outcome/$(@F)

generated/output/assignments/%.html: notes/assignments/%.tex resources/lesson-head.tex resources/discrete-math-packages.tex
	cd notes/assignments; pandoc --standalone --mathjax -f latex -t html $(<F) -o ../../generated/output/assignments/$(@F)

generated/output/activity-snippets/%.html: generated/notes/activity-snippets-flat/%.tex resources/lesson-head.tex resources/discrete-math-packages.tex
	cd generated/notes/activity-snippets-flat; pandoc --standalone --mathjax -f latex -t html $(<F) -o ../../output/activity-snippets/$(@F)

# Removing all auxiliary typesetting files from output directory and its subdirectories
clean-tex: 
	cd generated/output; rm -f *.out *.log *.aux
	cd generated/output/lessons; rm -f *.out *.log *.aux
	cd generated/output/app; rm -f *.out *.log *.aux
	cd generated/output/outcome; rm -f *.out *.log *.aux
	cd generated/output/assignments; rm -f *.out *.log *.aux
	cd generated/output/activity-snippets; rm -f *.out *.log *.aux

