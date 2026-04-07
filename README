# 🔍 Graph & Grid Algorithm Library

A clean, dependency-free Python library for common **BFS**, **DFS**, and **grid traversal** algorithms. Designed as a reliable toolkit for competitive programming, interview prep, and educational use.

---

## 📦 Modules

| File | Description |
|------|-------------|
| `bfs_lib.py` | BFS traversal, connectivity, shortest paths |
| `dfs_lib.py` | DFS traversal, cycle detection |
| `grid_bfs_lib.py` | Grid BFS — islands, pathfinding, distance problems |

---

## ⚙️ Implementation Conventions

Understanding these conventions is essential for using the library correctly.

### Error Handling — `-1` as Sentinel

All functions return **`-1`** when given invalid or degenerate input. This covers:
- Empty graph/grid (`{}`, `[]`)
- `start` node not present in the graph
- Out-of-bounds coordinates in grid functions
- Invalid board size (e.g. `n <= 0` for knight moves)
- Start or end cell being a wall in grid pathfinding

```python
bfs({}, 'A')           # → -1
shortest_path({}, 1, 2) # → -1
count_islands([])       # → -1
```

### No Path / No Result — `None`

When inputs are structurally valid but the goal is **unreachable**, functions return **`None`** (not `-1`):

```python
shortest_path(graph, 'A', 'Z')  # → None  (Z unreachable from A)
lee_algorithm(grid, (0,0), (3,3))  # → None  (blocked)
rotting_oranges(grid)  # → None  (some fresh oranges can never rot)
```

### Input Validation Scope

The library performs **only semantic validation** — it checks whether inputs make sense for the algorithm, not whether they conform to a type contract.

✅ **Checked:**
- Whether the graph is empty
- Whether `start`/`end` nodes exist in the graph
- Whether grid coordinates are in bounds
- Whether start/end cells are traversable (value `0`)

❌ **Not checked:**
- Whether `graph` is actually a `dict`
- Whether grid rows are all the same length
- Whether node values are hashable
- Whether `start`/`end` are tuples vs. lists in grid functions

If you pass malformed data (e.g., a list instead of a dict, or a grid with jagged rows), you will get a native Python exception, not a graceful `-1`.

---

## 📖 API Reference

### `bfs_lib.py`

#### Basic Traversal

```python
bfs(graph, start, visited=None) → set | -1
```
Returns the set of all nodes reachable from `start`. Accepts an optional `visited` set to continue a traversal across multiple calls.

```python
bfs_order(graph, start, visited=None) → list | -1
```
Returns nodes in BFS visit order. Also accepts an optional shared `visited` set.

```python
bfs_count(graph, start, visited=None) → int | -1
```
Returns the count of nodes reachable from `start`.

#### Connectivity

```python
normalize(graph) → dict
```
Converts a directed graph into an undirected one by adding reverse edges. Used internally; safe to call directly.

```python
is_connected_dir_undir_weak(graph, directed=False) → bool | -1
```
Returns `True` if the graph is (weakly) connected. Pass `directed=True` for directed graphs.

```python
count_components_dir_undir_weak(graph, directed=False) → int | -1
```
Returns the number of connected (or weakly connected) components.

```python
get_components_order_dir_undir_weak(graph, directed=False) → list[list] | -1
```
Returns a list of components, each as an ordered BFS traversal list.

```python
largest_component_size_dir_undir_weak(graph, directed=False) → int | -1
```
Returns the size of the largest component.

#### Shortest Paths

```python
shortest_path(graph, start, end) → list | None | -1
```
Returns the shortest path as a node list. Returns `[start]` if `start == end`. Returns `None` if no path exists.

```python
shortest_path_len(graph, start, end) → int | None | -1
```
Returns the length (number of edges) of the shortest path. Returns `0` if `start == end`.

```python
bidirectional_bfs_shortest_path_len_undirected(graph, start, end) → int | None | -1
```
Faster shortest path length using bidirectional BFS. Requires both `start` and `end` to be present in the graph.

---

### `dfs_lib.py`

```python
dfs(graph, start, visited=None) → set | -1
```
Recursive DFS. Returns the set of all visited nodes. Accepts an optional shared `visited` set.

```python
dfs_order(graph, start) → list | -1
```
Iterative DFS using an explicit stack. Returns nodes in DFS visit order. Note: does **not** accept a shared `visited` set — always starts fresh.

```python
has_cycle_directed(graph) → bool | -1
```
Detects cycles in a **directed** graph using the white/gray/black coloring method.

```python
has_cycle_undirected(graph) → bool | -1
```
Detects cycles in an **undirected** graph using parent tracking.

---

### `grid_bfs_lib.py`

> Grid convention: `0` = traversable cell, `1` = wall/obstacle (except `dist_to_nearest_one` and `rotting_oranges` which use domain-specific values).

#### Island Problems

```python
count_islands(grid) → int | -1
```
Counts the number of connected regions of `0`-cells (4-directional).

```python
get_islands_order(grid) → list[list[tuple]] | -1
```
Returns all islands as lists of `(row, col)` coordinates in BFS order.

```python
largest_island_area(grid) → int | -1
```
Returns the cell count of the largest island.

#### Pathfinding (Lee Algorithm)

```python
lee_algorithm(grid, start, end) → list[tuple] | None | -1
```
Finds the shortest path in a grid from `start` to `end`. Returns path as a list of `(row, col)` tuples. Returns `-1` for invalid input, `None` if unreachable.

```python
lee_algorithm_len(grid, start, end) → int | None | -1
```
Returns the length of the shortest grid path. Returns `0` if `start == end`.

#### Distance & Simulation

```python
dist_to_nearest_one(grid) → list[list[int]]
```
Multi-source BFS. Returns a grid where each cell contains its distance to the nearest `1`-cell. Cells that are `1` have distance `0`.

```python
rotting_oranges(grid) → int | None | -1
```
Simulates rotting spread (LeetCode 994). Grid values: `0` = empty, `1` = fresh orange, `2` = rotten orange. Returns minutes until all oranges rot, or `None` if impossible.

#### Knight Moves

```python
knight_moves(n, start, end) → list[tuple] | None | -1
```
Finds the shortest path for a chess knight on an `n×n` board. Returns path as `(row, col)` tuples.

```python
knight_moves_len(n, start, end) → int | None | -1
```
Returns the minimum number of moves for a knight to travel from `start` to `end`.

---

## 🗺️ Graph Format

All graph functions expect an **adjacency list** as a Python `dict`:

```python
# Directed graph
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}

# Undirected graph — edges must be listed both ways
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}
```

Nodes can be any hashable type (strings, integers, tuples, etc.).

## 🗺️ Grid Format

Grid functions expect a **2D list of integers**:

```python
grid = [
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 0],
]
```

Coordinates are always `(row, col)`. All movement is **4-directional** (up, down, left, right).

---

## 💡 Usage Examples

```python
from bfs_lib import shortest_path, count_components_dir_undir_weak
from dfs_lib import has_cycle_directed
from grid_bfs_lib import lee_algorithm, rotting_oranges

# Shortest path in an undirected graph
graph = {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}
print(shortest_path(graph, 1, 4))  # → [1, 2, 4]

# Count weakly connected components in a directed graph
dgraph = {'A': ['B'], 'B': [], 'C': ['D'], 'D': []}
print(count_components_dir_undir_weak(dgraph, directed=True))  # → 2

# Cycle detection
print(has_cycle_directed({'A': ['B'], 'B': ['A']}))  # → True

# Grid shortest path
grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
print(lee_algorithm(grid, (0, 0), (2, 2)))  # → [(0,0), (0,1), (0,2), (1,2), (2,2)]

# Rotting oranges
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(rotting_oranges(grid))  # → 4
```

---

## 📌 Quick Reference: Return Values

| Situation | Return Value |
|-----------|-------------|
| Invalid / empty input | `-1` |
| Valid input, goal unreachable | `None` |
| `start == end` (path functions) | `[start]` or `0` |
| Success | Result value or list |

---

## 📄 License

MIT