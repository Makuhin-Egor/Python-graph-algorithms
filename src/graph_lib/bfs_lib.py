from collections import deque

def bfs(graph, start, visited=None):
    if not graph:
        raise ValueError('Graph is empty!')
    if start not in graph:
        raise KeyError(f'Vertex {start} not in graph!')
    if visited == None:
        visited = set()
    visited.add(start)
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited

def bfs_order(graph, start, visited=None):
    if not graph:
        raise ValueError('Graph is empty!')
    if start not in graph:
        raise KeyError(f'Vertex {start} not in graph!')
    if visited == None:
        visited = set()
    visited.add(start)
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return order

def bfs_count(graph, start, visited=None):
    if not graph:
        raise ValueError('Graph is empty!')
    if start not in graph:
        raise KeyError(f'Vertex {start} not in graph!')
    if visited == None:
        visited = set()
    visited.add(start)
    queue = deque([start])
    size = 0
    while queue:
        node = queue.popleft()
        size += 1
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return size

def normalize(graph):
    undirected = {node: set(neighbours) for node, neighbours in graph.items()}
    for node, neighbours in graph.items():
        for nb in neighbours:
            undirected.setdefault(nb, set()).add(node)
    return undirected

def is_connected_dir_undir_weak(graph, directed=False):
    if not graph:
        raise ValueError('Graph is empty!')
    graph = normalize(graph) if directed else graph
    start = next(iter(graph))
    size = bfs_count(graph, start)
    return size == len(graph)

def count_components_dir_undir_weak(graph, directed=False):
    if not graph:
        raise ValueError('Graph is empty!')
    graph = normalize(graph) if directed else graph
    visited = set()
    count = 0
    for node in graph:
        if node not in visited:
            bfs(graph, node, visited)
            count += 1
    return count

def get_components_order_dir_undir_weak(graph, directed=False):
    if not graph:
        raise ValueError('Graph is empty!')
    graph = normalize(graph) if directed else graph
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            order = bfs_order(graph, node, visited)
            components.append(order)
    return components

def largest_component_size_dir_undir_weak(graph, directed=False):
    if not graph:
        raise ValueError('Graph is empty!')
    graph = normalize(graph) if directed else graph
    visited = set()
    max_size = 0
    for node in graph:
        if node not in visited:
            size = bfs_count(graph, node, visited)
            max_size = max(max_size, size)
    return max_size

def shortest_path(graph, start, end):
    if not graph:
        raise ValueError('Graph is empty!')
    if start not in graph:
        raise KeyError(f'Vertex {start} not in graph!')
    if start == end:
        return [start]
    visited = {start}
    queue = deque([start])
    parent = {start: None}
    while queue:
        node = queue.popleft()
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                parent[neighbour] = node
                if neighbour == end:
                    path = []
                    cur = end
                    while cur != None:
                        path.append(cur)
                        cur = parent[cur]
                    return path[::-1]
                visited.add(neighbour)
                queue.append(neighbour)
    return None

def shortest_path_len(graph, start, end):
    if not graph:
        raise ValueError('Graph is empty!') 
    if start not in graph:
        raise KeyError(f'Vertex {start} not in graph!')
    if start == end:
        return 0
    visited = {start}
    queue = deque([(start, 0)])
    while queue:
        node, dist = queue.popleft()
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                if neighbour == end:
                    return dist + 1
                visited.add(neighbour)
                queue.append((neighbour, dist + 1))
    return None

def bidirectional_bfs_shortest_path_len_undirected(graph, start, end):
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