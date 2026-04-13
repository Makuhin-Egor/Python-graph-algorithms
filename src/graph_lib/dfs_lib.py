def dfs(graph, start, visited=None):
    if not graph:
        raise ValueError('Graph is empty!')
    if start not in graph:
        raise KeyError(f'Vertex {start} not in graph!')
    if visited == None:
        visited = set()
    visited.add(start)
    for neighbour in graph.get(start, []):
        if neighbour not in visited:
            dfs(graph, neighbour, visited)
    return visited

def dfs_order(graph, start):
    if not graph:
        raise ValueError('Graph is empty!')
    if start not in graph:
        raise KeyError(f'Vertex {start} not in graph!')
    visited = {start}
    stack = [start]
    order = []
    while stack:
        node = stack.pop()
        order.append(node)
        for neighbour in reversed(graph.get(node, [])):
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)
    return order

def has_cycle_directed(graph):
    if not graph:
        raise ValueError('Graph is empty!')
    all_vertices = set(graph.keys())
    for neighbours in graph.values():
        all_vertices.update(neighbours)
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {v: WHITE for v in all_vertices}
    def dfs(node):
        color[node] = GRAY
        for neighbour in graph.get(node, []):
            if color[neighbour] == GRAY:
                return True
            if color[neighbour] == WHITE:
                if dfs(neighbour):
                    return True
        color[node] = BLACK
        return False
    return any(dfs(v) for v in all_vertices if color[v] == WHITE)

def has_cycle_undirected(graph):
    if not graph:
        raise ValueError('Graph is empty!')
    visited = set()
    def dfs(node, parent):
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour == parent:
                continue
            if neighbour in visited:
                return True
            if dfs(neighbour, node):
                return True
        return False
    return any(dfs(node, None) for node in graph if node not in visited)
