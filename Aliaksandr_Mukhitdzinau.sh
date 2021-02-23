#!/bin/bash

#Python versions
python2='2.7.18'
python3='3.7.8'

#Installing python versions 2.7 and 3.7
pyenv install -s $python3 && pyenv install -s $python2

#Installing pyenv-virtualenv(required for creating virtual environments)
git clone http://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv || echo 'pyenv-virtualenv already installed'

#Creating virtual environments
pyenv virtualenv -f $python2 python2env && pyenv virtualenv -f $python3 python3env
