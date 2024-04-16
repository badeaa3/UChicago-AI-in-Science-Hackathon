import networkx as nx
import shelve


with shelve.open("la.shelf") as train_shelf:
    print(f"We have {len(train_shelf.keys())} molecular graphs to train with\n")

    for smiles_string in train_shelf:
        print("Our first data point is described by this SMILES string: ", smiles_string)
        print("SMILES is described in detail here https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system\n")

        graph = train_shelf[smiles_string]
        print("The training data is the format of networkx graphs: ", graph)
        print("All graphs are guaranteed to have less then 100 nodes, but there is no absolute limit on the number of edges.\n")

        print("Let's take a look on how the nodes are organized.")
        for node in graph.nodes(data=True):
            print(node, "\n")

            print("The first index is just a label for the node {node[0]}.")
            print("But keep in mind, that there is no meaning to this index,\n"
                  "your result should be identical if these indeces are permuted.\n"
                  "Permutation Invariance!\n")

            print("The following attributes are readily available to you, you may use them to featurize your nodes in the Graph for training.\n"
                  "They are considered input, you do not have to learn them.")
            print("They do have chemical meaning, you can decide how much of that meaning you use to algorithm.")
            for attr in ['atomic', 'valence', 'formal_charge', 'aromatic', 'hybridization']:
                print(attr, node[1][attr])

            print("\n")
            print("'atomic' is the atomic number, so the index of the periodic table, or the number of protons in the core.")
            print("This number tells apart the different elements, for example 6 is carbon and 1 is hydrogen.\n")

            print("The last attribute 'param' is the ouput for this challenge.\n"
                  " It is provided for the training and testing set only for supervised learning procedures.\n"
                  "You are not allowed to use them as input ever!\n"
                  )
            print("Exception: if you want for example the 'mass' as input feature for your 'epsilon' training, you MUST use the 'mass' value that is the output of your model for predicting 'mass'\n")

            print("The following are simple scalar values, that can be directly predictied:\n")
            for key in ['mass', 'charge', 'sigma', 'epsilon']:
                print(key, node[1]["param"][key])





            # We don't want to print all info of all nodes here.
            break


        # We don't want to print every data point here.
        break
