# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    		?= -b dirhtml
SPHINXBUILD   		?= sphinx-build
SOURCEDIR     		= source
BUILDDIR      		= build
GITHUB_PAGES_BRANCH = gh-pages

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

live:
	@sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

deploy: html
	git config --global user.email "noreply@python.org.br"
	git config --global user.name "apyb-bot"
	ghp-import -m "Deploy apyb/wiki" -b $(GITHUB_PAGES_BRANCH) $(BUILDDIR)/html/
	git push -fq origin $(GITHUB_PAGES_BRANCH) > /dev/null

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
