# make → opens the main notebook
# make main → same
# make nn → opens the NN-only notebook

# make install → sets up venv + deps
# make test → runs pytest

# make clean → deletes venv + caches



PYTHON       = python3
VENV_DIR     = venv
PIP          = $(VENV_DIR)/bin/pip
PYTHONBIN    = $(VENV_DIR)/bin/python
JUPYTER      = $(VENV_DIR)/bin/jupyter

MAIN_NOTEBOOK = All_models_and_visualizations.ipynb
NN_NOTEBOOK   = softmaxNN.ipynb

.PHONY: all install main nn run test clean help

all: main

install: $(VENV_DIR)/bin/activate
	$(PIP) install -r requirements.txt

$(VENV_DIR)/bin/activate: requirements.txt
	$(PYTHON) -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip
	touch $@

main: install
	$(JUPYTER) notebook $(MAIN_NOTEBOOK)

nn: install
	$(JUPYTER) notebook $(NN_NOTEBOOK)

run: main

test: install
	$(PYTHONBIN) -m pytest

clean:
	rm -rf $(VENV_DIR)
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .+$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[1m%-10s\033[0m %s\n", $$1, $$2}'
