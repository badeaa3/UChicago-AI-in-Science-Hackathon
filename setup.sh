#!/bin/bash

PREFIX=/project/dfreedman/colmt/anaconda/hackathon

# Make sure that conda is available, this is specific to midway3
. /software/python-anaconda-2022.05-el8-x86_64/etc/profile.d/conda.sh

# Create the conda base environment, I do this with mamba because conda wasn't behaving
mamba create --prefix=$PREFIX python=3.11

# Activate the new environment
conda activate $PREFIX

# Install the packages with pip
pip install -r requirements.txt

echo "New environment available at $PREFIX"

