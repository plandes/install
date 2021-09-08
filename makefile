## makefile automates the build and deployment for python projects

## build config

# type of project
PROJ_TYPE =		python
# make modules to add functionality to a build
PROJ_MODULES =		git python-resources python-cli python-doc python-doc-deploy
INFO_TARGETS +=		appinfo

include ./zenbuild/main.mk

.PHONY:			appinfo
appinfo:
			@echo "app-resources-dir: $(RESOURCES_DIR)"
