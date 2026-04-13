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
