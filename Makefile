pyVersion = 3.7.3

VENV_NAME?=venv
venv: $(VENV_NAME)/bin/activate

all: pyenv pyenv-install venv/bin/activate ## Fire and forget boys.
	echo "All done."

venv/bin/activate: 
	text -d venv || python -m venv venv
	venv/bin/pip3 install -U pip

instabot-py: venv ## Installs instabot-py
	venv/bin/pip3 install instabot-py

instapy: venv ## Installs instapy
	venv/bin/pip3 install instapy

instapy-pi: instapy ## Installs instapy on raspberri
	venv/bin/pip3 uninstall instapy-chromedriver
	venv/bin/pip3 install instapy-chromedriver==2.36post0

pyenv: pyenv-dev ## installs pyenv - "run: pyenv install after" 
	curl https://pyenv.run | bash
	pyenv install --list | grep -v '[a-z,0-2]'

pyenv-install: ## installs latest python version. Restart terminal window after running this command
	pyenv install $(pyVersion)
	pyenv global $(pyVersion)
	echo "Restart the terminal window for changes to take effect"

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
