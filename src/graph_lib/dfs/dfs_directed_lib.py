__all__ = ['has_cycle_directed', 'topological_sort']

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

def topological_sort(graph):
    if not graph:
        raise ValueError('Graph is empty!')
    all_vertices = set(graph.keys())
    for neighbours in graph.values():
        all_vertices.update(neighbours)
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {v: WHITE for v in all_vertices}
    order = []
    def dfs(node):
        color[node] = GRAY
        for neighbour in graph.get(node, []):
            if color[neighbour] == GRAY:
                raise ValueError('Has cycle!')
            if color[neighbour] == WHITE:
                dfs(neighbour)
        color[node] = BLACK
        order.append(node)
    for node in all_vertices:
        if color[node] == WHITE:
            dfs(node)
    return order[::-1]