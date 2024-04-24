import networkx as nx
import json
import numpy as np
import copy
import hashlib

from util import SEED, SMI

from helper import load_data_from_file, write_data_to_json_file


def remove_param(graph):
    for i in range(len(graph)):
        del graph.nodes[i]["param"]
    return graph

def get_permutation(n, rng):
    permutation = np.asarray(range(n), dtype=int)
    rng.shuffle(permutation)
    return permutation

def get_inv_permutation(permutation):
    inv_permutation = np.argsort(permutation)
    return inv_permutation

def apply_permutation(graph, permutation):
    new_graph = nx.Graph()
    for node in graph.nodes(data=True):
        new_idx = int(permutation[node[0]])
        attrs = node[1]
        new_graph.add_node(new_idx, **attrs)

    for edge in graph.edges(data=True):
        a = int(permutation[edge[0]])
        b = int(permutation[edge[1]])
        attrs = edge[2]
        new_graph.add_edge(a, b, **attrs)
    return new_graph


def write_out_data(data_in):
    data_out = {}
    for smi in data_in:
        m = hashlib.shake_256()
        m.update(bytes(smi, "utf-8"))
        name = m.hexdigest(10)
        graph = remove_param(copy.deepcopy(data_in[smi]))
        data_out[name] = graph
    write_data_to_json_file(data_out, "validation_masked.json")

def write_perm_data(data_in):
    perm_graphs = {}
    smi=SMI
    graph = data_in[smi]
    half_graph = remove_param(copy.deepcopy(graph))
    rng = np.random.default_rng(seed=SEED)
    permutation_dict = {}
    for _ in range(50):
        perm = get_permutation(len(half_graph), rng)
        m = hashlib.shake_256()
        m.update(perm.tobytes())
        name = m.hexdigest(10)
        permutation_dict[name] = [int(e) for e in perm]

        permuted_graph = apply_permutation(half_graph, perm)
        perm_graphs[name] = permuted_graph
    with open("permutations.json", "w") as json_handle:
        json.dump(permutation_dict, json_handle)
    write_data_to_json_file(perm_graphs, "permutation_masked.json")

def main():
    data_in = load_data_from_file("competition.json")
    write_out_data(data_in)
    write_perm_data(data_in)


    # inv_perm = get_inv_permutation(perm)
    # new_graph = apply_permutation(graph, perm)
    # new_graph2 = apply_permutation(new_graph, inv_perm)

    # found_diff = False
    # for node in graph.nodes(data=True):
    #     assert node[1] == new_graph.nodes(data=True)[perm[node[0]]]
    #     assert node[1] == new_graph2.nodes(data=True)[node[0]]
    #     if node[1] != new_graph.nodes(data=True)[node[0]]:
    #         found_diff = True
    # assert found_diff

    # for edge in graph.edges(data=True):
    #     print(edge[2])




if __name__ == "__main__":
    main()
