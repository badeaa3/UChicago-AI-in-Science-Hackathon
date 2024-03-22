#!/bin/bash

# Define the virtual environment name and the custom index URL
VENV_NAME="work"
current_directory=$(pwd)

# Create the virtual environment
python3 -m venv $VENV_NAME

# Activate the virtual environment
source $VENV_NAME/bin/activate

# upgrade pip
pip install --upgrade pip

# install the packages
pip install -r requirements.txt

# deactivate venv
deactivate

# export VENV_NAME to activate environment
echo "alias work='source ${current_directory}/$VENV_NAME/bin/activate'" >> ~/.bash_profile
source ~/.bash_profile
echo "from now on type the following to turn on the virtual environment: work"
