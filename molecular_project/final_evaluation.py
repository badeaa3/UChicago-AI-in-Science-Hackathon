import networkx as nx
import numpy as np
import helper
import hashlib
import copy
import json

from make_permutation import get_inv_permutation, apply_permutation

def compare_property(property_name:str, result_dict, ref_dict, max_node_size:int=100):
    def get_graph_property_data(property_name, graph):
        data = np.zeros(max_node_size)
        for node in graph.nodes(data=True):
            data[node[0]] = node[1]["param"][property_name]
        return data
    result_data = []
    ref_data = []

    miss_counter = 0
    for smi in ref_dict:
        m = hashlib.shake_256()
        m.update(bytes(smi, "utf-8"))
        name = m.hexdigest(10)
        if name not in result_dict:
            miss_counter += 1
        else:
            result_data.append(get_graph_property_data(property_name, result_dict[name]))
            ref_data.append(get_graph_property_data(property_name, ref_dict[smi]))
    result_data = np.asarray(result_data)
    ref_data = np.asarray(ref_data)

    negative_counter = np.sum(ref_data < 0)

    print(f"\nAnalysis for {property_name}")
    print(f"# Missing Molecules: {miss_counter}")
    print(f"# Negative values detected: {negative_counter}")

    sq_diff = (result_data - ref_data)**2
    print(f"Root Mean Squared Difference: {np.sqrt(np.mean(sq_diff))}")
    print(f"Max difference: {np.sqrt(np.max(sq_diff))}")
    print("\n")


def add_data_from_prediction(result_dict, rng):
    """
    This function simulates adding data to a final graph.
    Do not use this function.
    Use your model to do the prediction and then fill it in.
    """
    def get_random_param(rng):
        param = {}
        param["epsilon"] = rng.random()
        param["mass"] = rng.random()
        param["sigma"] = rng.random()
        param["charge"] = rng.normal()
        return param

    for name in result_dict:
        graph = result_dict[name]
        for node in graph.nodes(data=True):
            node[1]["param"] = get_random_param(rng)
            graph.update(nodes=[node])

    # Remove a graph for good measure
    del result_dict[name]
    # Add a different graph
    result_dict["asdf"] = graph

def compare_permutation(property_name:str, result_dict, ref_graph, permutation_dict, max_node_size:int=100):
    def get_graph_property_data(property_name, graph):
        data = np.zeros(max_node_size)
        for node in graph.nodes(data=True):
            data[node[0]] = node[1]["param"][property_name]
        return data
    result_data = []
    ref_data = []

    miss_counter = 0
    for name in permutation_dict:
        perm = np.asarray(permutation_dict[name], dtype=int)
        if name not in result_dict:
            miss_counter += 1
        else:
            inv_permutation = get_inv_permutation(perm)
            graph = result_dict[name]
            inv_graph = apply_permutation(graph, inv_permutation)

            # Check that inverting the permutation worked
            for node in ref_graph.nodes(data=True):
                ref_attr = copy.deepcopy(node[1])
                del ref_attr["param"]
                result_attr = copy.deepcopy(inv_graph.nodes(data=True)[node[0]])
                del result_attr["param"]

                assert ref_attr == result_attr

            result_data.append(get_graph_property_data(property_name, inv_graph))
            ref_data.append(get_graph_property_data(property_name, ref_graph))
    result_data = np.asarray(result_data)
    ref_data = np.asarray(ref_data)

    negative_counter = np.sum(ref_data < 0)

    print(f"\nAnalysis for {property_name}")
    print(f"# Missing Molecules: {miss_counter}")
    print(f"# Negative values detected: {negative_counter}")

    sq_diff = (result_data - ref_data)**2
    print(f"Root Mean Squared Difference: {np.sqrt(np.mean(sq_diff))}")
    print(f"Max difference: {np.sqrt(np.max(sq_diff))}")
    print("\n")




def main():
    from util import SEED, SMI
    # You won't necessarily have this data available
    ref_dict = helper.load_data_from_file("competition.json")


    result_dict = helper.load_data_from_file("validation_masked.json")
    # In a real case, we would not add random results.
    # Instead you would fill it with your results and then write it to disk to hand it to us.
    # This is for mock up testing only.
    rng = np.random.default_rng(seed=SEED)
    add_data_from_prediction(result_dict, rng)

    compare_property("epsilon", result_dict, ref_dict)
    compare_property("mass", result_dict, ref_dict)
    compare_property("sigma", result_dict, ref_dict)
    compare_property("charge", result_dict, ref_dict)


    print("Permutation check")
    ref_graph = ref_dict[SMI]
    result_perm_dict = helper.load_data_from_file("permutation_masked.json")
    with open("permutations.json", "r") as json_handle:
        permutation_dict = json.load(json_handle)
    add_data_from_prediction(result_perm_dict, rng)

    compare_permutation("epsilon", result_perm_dict, ref_graph, permutation_dict)
    compare_permutation("mass", result_perm_dict, ref_graph, permutation_dict)
    compare_permutation("sigma", result_perm_dict, ref_graph, permutation_dict)
    compare_permutation("charge", result_perm_dict, ref_graph, permutation_dict)




if __name__ == "__main__":
    main()
