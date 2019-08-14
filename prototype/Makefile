VENV ?= env
PIP ?= $(VENV)/bin/pip

help:
	@echo "  help         this list"
	@echo "  clean        delete virtualenv directory $(VENV)"
	@echo "  prepare-venv install virtualenv and requiements into directory $(VENV)"

clean:
	rm -rf env

prepare-venv:
	pip install virtualenv
	virtualenv $(VENV)
	$(PIP) install -r requirements.txt
