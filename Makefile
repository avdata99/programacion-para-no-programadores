# You can set these variables from the command line.
SPHINXOPTS    =
SOURCEDIR     = source
BUILDDIR      = docs
BUILDFORMATS  = $(BUILDDIR)/formats

# like conf.py
EXPORT-NAME    = Curso-Python

.PHONY: default view clean html epub mobi pdf

default: html

all: html pdf epub mobi

view:
	xdg-open $(BUILDDIR)/index.html

clean:
	-rm -rf $(BUILDDIR)/*

html:
	sphinx-build -b html $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)

epub:
	sphinx-build -b epub $(SPHINXOPTS) $(SOURCEDIR) $(BUILDFORMATS)/epub
	mv $(BUILDFORMATS)/epub/$(EXPORT-NAME).epub $(BUILDDIR)/$(EXPORT-NAME).epub
	rm -rf $(BUILDFORMATS)/epub

pdf:
	rm -rf $(BUILDFORMATS)/latex
	sphinx-build -b latex $(SPHINXOPTS) $(SOURCEDIR) $(BUILDFORMATS)/latex
	
	cd $(BUILDFORMATS)/latex && make
	mv $(BUILDFORMATS)/latex/$(EXPORT-NAME).pdf $(BUILDDIR)/$(EXPORT-NAME).pdf
	mv $(BUILDFORMATS)/latex/$(EXPORT-NAME).tex $(BUILDDIR)/$(EXPORT-NAME).tex
	rm -rf $(BUILDFORMATS)/latex
