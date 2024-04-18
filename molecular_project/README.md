# Explanation of the Dataset and Challenge

This sub-directory contains data and some initial code to help you get started. We utilize the Python `json` module to store the training data. You can access all the data for this challenge within the `data.json`.
We have the python module `helper.py` that helps to read and write dictionaries of graphs.

The JSON is structured in key-value pairs, where the key is the SMILES string of the molecule used for training. The value is a networkx graph, which includes attributes on nodes and edges that serve as inputs and outputs for your models. Please refer to and execute `explain_graph_data.py` for a more detailed understanding of the data.

## Extra Information

The following data is not necessary for completing the initial challenges.

The forcefield we aim to parameterize is [OPLS](https://doi.org/10.1021/ja9621760). Additionally, we provide an `opls.par` file that defines SMARTS rules for identifying OPLS types in molecules. We have already used these rules to assign all types and values, so further exploration on your part is likely unnecessary.

The file `ffnonbonded.itp` outlines the values for the forcefield based on the determined OPLS types. We have already performed this lookup, so you will not need to refer to this file.

The `ffbonded.itp` file specifies bonded parameters for bonds, angles, and dihedrals between atoms. This aspect is more complex; hence our dataset only includes bond types for classification purposes. In later, more advanced challenges, you may need to refer to this file to obtain initial input values for predictions on bonds, angles, and dihedrals directly.

## How We Prepared the Data

If you are curious about how we prepared the data, you can look into `prep_data.py`. However, this script will not execute on your system, as we have obscured the specifics of how we obtain and shuffle the SMILES strings to create the training and competition datasets. Therefore, you should not attempt to run this file. The `requirements_prepare.txt` file lists the `pip` requirements exclusively for this script, which are not necessary for solving the challenge.