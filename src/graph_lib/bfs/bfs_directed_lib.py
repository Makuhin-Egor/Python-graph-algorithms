__all__ = ['normalize', 'is_connected_directed', 'count_components_directed', \
'get_components_order_directed', 'largest_component_size_directed']

from .bfs_general_lib import *

def normalize(graph):
    undirected = {node: set(neighbours) for node, neighbours in graph.items()}
    for node, neighbours in graph.items():
        for nb in neighbours:
            undirected.setdefault(nb, set()).add(node)
    return undirected

def is_connected_directed(graph):
    if not graph:
        raise ValueError('Graph is empty!')
    graph = normalize(graph)
    start = next(iter(graph))
    size = bfs_count(graph, start)
    return size == len(graph)

def count_components_directed(graph):
    if not graph:
        raise ValueError('Graph is empty!')
    graph = normalize(graph)
    visited = set()
    count = 0
    for node in graph:
        if node not in visited:
            bfs(graph, node, visited)
            count += 1
    return count

def get_components_order_directed(graph):
    if not graph:
        raise ValueError('Graph is empty!')
    graph = normalize(graph)
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            order = bfs_order(graph, node, visited)
            components.append(order)
    return components

def largest_component_size_directed(graph):
    if not graph:
        raise ValueError('Graph is empty!')
    graph = normalize(graph)
    visited = set()
    max_size = 0
    for node in graph:
        if node not in visited:
            size = bfs_count(graph, node, visited)
            max_size = max(max_size, size)
    return max_size