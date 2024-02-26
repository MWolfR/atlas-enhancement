# path to executable
METRICS_COVERAGE_BIN := $(PYTHON3) $(SOURCE_CODE_ROOT)/metrics/coverage.py

# DO NOT EDIT BELOW THIS LINE
override INPUTS := input/$(RELATIVE_DEPTH_FILE)\
	input/$(FLATMAP_NRRD_FILE)

override OUTPUTS := output/$(METRICS_COVERAGE_FILE)

override USER_PARAMETERS :=

override USER_BINARIES := METRICS_COVERAGE_BIN
