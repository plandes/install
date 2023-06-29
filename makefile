## makefile automates the build and deployment for python projects

## build config

# type of project
PROJ_TYPE =		python
# make modules to add functionality to a build
PROJ_MODULES =		git python-resources python-cli python-doc python-doc-deploy markdown
INFO_TARGETS +=		appinfo
CLEAN_DEPS +=		cleanexample

#PY_SRC_TEST_PAT =	'test_d*.py'

include ./zenbuild/main.mk

.PHONY:			appinfo
appinfo:
			@echo "app-resources-dir: $(RESOURCES_DIR)"

.PHONY:			cleanexample
cleanexample:
			find example -type d -name __pycache__ \
			  -prune -exec rm -r {} \;
