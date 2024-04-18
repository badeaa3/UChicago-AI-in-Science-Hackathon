import networkx as nx
import numpy as np
import helper

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
        if smi not in result_dict:
            miss_counter += 1
        else:
            result_data.append(get_graph_property_data(property_name, result_dict[smi]))
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
    print(f"Min difference: {np.sqrt(np.min(sq_diff))}")
    print("\n")


def main():
    ref_dict = helper.load_data_from_file("data.json")
    # For demonstration only. Use your real results here!
    result_dict = helper.load_data_from_file("data.json")

    compare_property("epsilon", result_dict, ref_dict)
    compare_property("mass", result_dict, ref_dict)
    compare_property("sigma", result_dict, ref_dict)
    compare_property("charge", result_dict, ref_dict)

if __name__ == "__main__":
    main()
