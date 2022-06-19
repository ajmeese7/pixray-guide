#!/bin/bash

###
# Modified from the following links:
# https://github.com/lucidrains/deep-daze/issues/80#issuecomment-798855778
# https://colab.research.google.com/github/pixray/pixray_notebooks/blob/master/pixray_simple.ipynb
###

python3 -m pip install virtualenv
python3 -m virtualenv .venv
source .venv/bin/activate
echo "You should be in a clean python virtual environment now. Packages installed here won't pollute your global python. Everytime you want to work on this project again, you will need to run 'source .venv/bin/activate' again. "

# Ensure that you are in a clean virtual environment
which python
echo "Your python path should have '.venv' in it by now. If its from /usr/local/bin, /usr/bin, or /bin, you need to run 'source .venv/bin/activate' again inside your project directory."

# Install pixray
git clone --recursive https://github.com/pixray/pixray
cd pixray
pip install -r requirements.txt
pip install basicsr
git clone https://github.com/pixray/diffvg
cd diffvg
git submodule update --init --recursive
python setup.py install
cd ..
