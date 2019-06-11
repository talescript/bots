install: pyenv .venv ## Activate venv and install dependencies
	pip install -U pip
	pip install instapy

VENV = .venv
export VIRTUAL_ENV := $(abspath ${VENV})
export $PATH := ${VIRTUAL_ENV}/bin:${PATH}

${VENV}:
	python -m venv $@

pyenv: pyenv-dev pyenv-install ## installs pyenv - "run: pyenv install -v <version.number>" 
	curl https://pyenv.run | bash
	exec "$SHELL"
	pyenv install --list | grep " 3\.[789]" | grep -v "dev"

pyenv-dev: ## development prerequisites (debian)
	sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
		libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
		xz-utils tk-dev libffi-dev liblzma-dev python-openssl git -y

pyenv-libedit: ## alternative to libreadline-dev
	sudo apt install libedit-dev -y

pyenv-install: # installs latest python version
	pyenv install 3.7.3
	pyenv global 3.7.3

pyenv-update: ## update pyenv
	pyenv update

pyenv-delete: ## delete pyenv
	rm -fr ~/.pyenv

clean: ## Removes __pycache__
	rm -rf __pycache__

.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

