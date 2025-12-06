## makefile automates the build and deployment for python projects


## Build system
#
PROJ_TYPE =		python
PROJ_MODULES =		python/doc python/package python/deploy
CLEAN_ALL_DEPS +=	cleanexample


## Project
#
EXAMPLE_DIR =		example


## Includes
#
include ./zenbuild/main.mk


## Functions
#
# run the example
define example
	$(call loginfo,running: $(1))
	@( cd $(EXAMPLE_DIR) ; \
	   PYTHONPATH="$${PYTHONPATH:+$${PYTHONPATH}:}../src" \
	   $(PY_PX_BIN) run python app.py $(1) )
endef


## Targets
#
.PHONY:			runexample
runexample:		$(PY_PYPROJECT_FILE)
			$(call example)

.PHONY:			cleanexample
cleanexample:		$(PY_PYPROJECT_FILE)
			$(call logininfo,removing example files)
			$(call example,clean)
			$(call loginfo,removing example derived objects)
			@find $(EXAMPLE_DIR) -type d -name __pycache__ \
			  -prune -exec rm -r {} \;
