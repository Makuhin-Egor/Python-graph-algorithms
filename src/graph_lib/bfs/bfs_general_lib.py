__all__ = ['bfs', 'bfs_order', 'bfs_count', 'bfs_distances', 'shortest_path', \
'shortest_path_len', 'deque']

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

def bfs_distances(graph, start):
    if not graph:
        raise ValueError('Graph is empty!')
    if start not in graph:
        raise KeyError(f'Vertex {start} not in graph!')
    distances = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbour in graph[node]:
            if neighbour not in distances:
                distances[neighbour] = distances[node] + 1
                queue.append(neighbour)
    return distances

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