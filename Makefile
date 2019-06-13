pyVersion = 3.7.3

VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

install: pyenv pyenv-install  ## Activate venv and install dependencies
	( \
		python -m venv venv; \
		. venv/bin/activate; \
		pip install -U pip; \
		pip install instapy; \
		)

venv: $(VENV_NAME)/bin/activate
venv/bin/activate: requirements.txt
	text -d venv || . venv/bin/activate
	venv/bin/pip3 install -U pip
	venv/bin/pip3 install instapy
	touch venv/bin/activate


pyenv: pyenv-dev ## installs pyenv - "run: pyenv install after" 
	curl https://pyenv.run | bash
	pyenv install --list | grep -v '[a-z,0-2]'

pyenv-install: ## installs latest python version
	pyenv install $(pyVersion)
	pyenv global $(pyVersion)

pyenv-update: ## update pyenv
	pyenv update

pyenv-delete: ## delete pyenv
	-rm -fr ~/.pyenv

pyenv-dev: ## development prerequisites (debian)
	sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
		libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
		xz-utils tk-dev libffi-dev liblzma-dev python-openssl git -y

pyenv-libedit: ## alternative to libreadline-dev
	sudo apt install libedit-dev -y

clean: ## Removes __pycache__
	-rm -rf __pycache__

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
.PHONY: help install clean pyenv pyenv-install pyenv-update \
   	pyenv-delete pyenv-dev
