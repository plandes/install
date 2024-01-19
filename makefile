## makefile automates the build and deployment for python projects


## Build system
#
PROJ_TYPE =		python
PROJ_MODULES =		git python-resources python-cli python-doc python-doc-deploy markdown
CLEAN_DEPS +=		cleanexample


## Includes
#
include ./zenbuild/main.mk


## Targets
#
.PHONY:			cleanexample
cleanexample:
			find example -type d -name __pycache__ \
			  -prune -exec rm -r {} \;
