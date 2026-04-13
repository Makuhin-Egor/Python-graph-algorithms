from bfs_general_lib import *

def is_connected_undirected(graph):
    if not graph:
        raise ValueError('Graph is empty!')
    start = next(iter(graph))
    size = bfs_count(graph, start)
    return size == len(graph)

def count_components_undirected(graph):
    if not graph:
        raise ValueError('Graph is empty!')
    visited = set()
    count = 0
    for node in graph:
        if node not in visited:
            bfs(graph, node, visited)
            count += 1
    return count

def get_components_order_undirected(graph):
    if not graph:
        raise ValueError('Graph is empty!')
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            order = bfs_order(graph, node, visited)
            components.append(order)
    return components

def largest_component_size_undirected(graph):
    if not graph:
        raise ValueError('Graph is empty!')
    visited = set()
    max_size = 0
    for node in graph:
        if node not in visited:
            size = bfs_count(graph, node, visited)
            max_size = max(max_size, size)
    return max_size

def shortest_path_len_undirected(graph, start, end):
    if not graph:
        raise ValueError('Graph is empty!')
    if start not in graph:
        raise KeyError(f'Vertex {start} not in graph!')
    if end not in graph:
        raise KeyError(f'Vertex {end} not in graph!')
    if start == end:
        return 0
    dict_s = {start: 0}
    dict_e = {end: 0}
    queue_s = deque([start])
    queue_e = deque([end])
    while queue_s or queue_e:
        if queue_s:                        
            for _ in range(len(queue_s)):
                node = queue_s.popleft()
                for neighbour in graph[node]:
                    if neighbour not in dict_s:
                        dict_s[neighbour] = dict_s[node] + 1
                        queue_s.append(neighbour)
            common = dict_s.keys() & dict_e.keys()
            if common:
                return min(dict_s[node] + dict_e[node] for node in common)            
        if queue_e:
            for _ in range(len(queue_e)):
                node = queue_e.popleft()
                for neighbour in graph[node]:
                    if neighbour not in dict_e:
                        dict_e[neighbour] = dict_e[node] + 1
                        queue_e.append(neighbour)
            common = dict_s.keys() & dict_e.keys()
            if common:
                return min(dict_e[node] + dict_s[node] for node in common)
    return None