PYTHON    = python3
VENV_DIR  = venv
PIP       = $(VENV_DIR)/bin/pip
PYTHONBIN = $(VENV_DIR)/bin/python
JUPYTER   = $(VENV_DIR)/bin/jupyter
NOTEBOOK  = nba_champion_models.ipynb #replace this with full ipynb name

.PHONY: all install notebook run test clean help

all: notebook

install: $(VENV_DIR)/bin/activate
	$(PIP) install -r requirements.txt

$(VENV_DIR)/bin/activate: requirements.txt
	$(PYTHON) -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip
	touch $@

notebook: install
	$(JUPYTER) notebook $(NOTEBOOK)

run: notebook

test: install
	$(PYTHONBIN) -m pytest

clean:
	rm -rf $(VENV_DIR)
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .+$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[1m%-10s\033[0m %s\n", $$1, $$2}'
