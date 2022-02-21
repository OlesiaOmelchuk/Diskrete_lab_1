"""Kruskal's algorithm"""
import random
from itertools import combinations, groupby
import networkx as nx
import matplotlib.pyplot as plt


def gnp_random_connected_graph(num_of_nodes: int,
                               completeness: int,
                               draw: bool = False) -> list[tuple[int, int]]:
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi 
    graph, but enforcing that the resulting graph is conneted
    """
    weight_list = []

    edges = combinations(range(num_of_nodes), 2)
    G = nx.Graph()
    G.add_nodes_from(range(num_of_nodes))

    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < completeness:
                G.add_edge(*e)

    for (u, v, w) in G.edges(data=True):
        w['weight'] = random.randint(0, 10)
        weight_list.append(w['weight'])

    if draw:
        plt.figure(figsize=(10, 6))
        nx.draw(G, node_color='lightblue',
                with_labels=True,
                node_size=500)

    return G, weight_list


def kruskal(graph_and_weight: tuple) -> list[tuple]:
    """
    Get minimum spanning tree using Kruskal's algorithm.
    Returns: list of nodes.
    """
    carcass_edges = []

    G = graph_and_weight[0]
    edges = list(G.edges())
    num_of_nodes = len(G.nodes())
    weights = graph_and_weight[1]

    nodes = [{i} for i in range(num_of_nodes)]
    weights_edges = {}
    for i in range(len(weights)):
        weights_edges[edges[i]] = weights[i]
    weights_edges_sorted = sorted(weights_edges.items(), key=lambda x: x[1])

    for edge in weights_edges_sorted:
        node_1 = edge[0][0]
        node_2 = edge[0][1]
        sets_to_union = []
        for group in nodes:
            if node_1 in group and node_2 in group:
                break
            elif node_1 in group or node_2 in group:
                sets_to_union.append(group)

        if sets_to_union:
            carcass_edges.append(edge[0])
            nodes.append(sets_to_union[0].union(sets_to_union[1]))
            nodes.remove(sets_to_union[0])
            nodes.remove(sets_to_union[1])

    return carcass_edges


if __name__ == '__main__':
    random_graph = gnp_random_connected_graph(500, 0.6)
    minimum_tree = kruskal(random_graph)
    print(minimum_tree)
