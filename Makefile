
# Makefile
SHELL := /bin/bash

.PHONY: help
help:
	@echo "Commands:"
	@echo "venv    : creates development environment."
	@echo "install : Installs all packages."
	@echo "style   : runs style formatting."
	@echo "clean   : cleans all unnecessary files."
	@echo "test    : runs all tests."


# Environment
.ONESHELL:
venv:
	python3 -m venv venv

# Install
.PHONY: install
install:
		python -m pip install --upgrade pip
		pip install -r requirements.txt

# Style
.PHONY: style
style:
		flake8

# Cleaning
.PHONY: clean
clean:
	rm -rf venv
	find . -type f -name "*.DS_Store" -ls -delete
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
	find . | grep -E ".pytest_cache" | xargs rm -rf
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf
	rm -f .coverage

# Test
.PHONY: test
test:
	python manage.py test -v2