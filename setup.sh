#!/bin/bash

# load rcc modules
module load python/miniforge-24.1.2 # python 3.10

# Define the virtual environment name and the custom index URL
VENV_NAME="hackathon"
current_directory=$(pwd)

# check if directory exists
if test -d $VENV_NAME; then
  source $VENV_NAME/bin/activate
else

  # Create the virtual environment
  python3 -m venv $VENV_NAME

  # Activate the virtual environment
  source $VENV_NAME/bin/activate

  # upgrade pip
  pip install --upgrade pip

  # install the packages
  pip install -r requirements.txt
fi
