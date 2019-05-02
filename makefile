SHELL := /bin/bash
# /bin/bash is needed to activate the venv

install:
	python -m venv venv
	source venv/bin/activate
	pip install -U pip
	pip install instapy

