from collections import deque

def count_islands(grid):
    if not grid:
        return -1
    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * cols for _ in range(rows)]
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and not visited[r][c]:
                visited[r][c] = True
                queue = deque([(r, c)])
                count += 1
                while queue:
                    cr, cc = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows\
                        and 0 <= nc < cols\
                        and grid[nr][nc] == 0\
                        and not visited[nr][nc]:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
    return count

def get_islands_order(grid):
    if not grid:
        return -1
    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * cols for _ in range(rows)]
    islands = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and not visited[r][c]:
                visited[r][c] = True
                queue = deque([(r, c)])
                island = []
                while queue:
                    cr, cc = queue.popleft()
                    island.append((cr, cc))
                    for dr, dc in directions:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows\
                        and 0 <= nc < cols\
                        and grid[nr][nc] == 0\
                        and not visited[nr][nc]:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
                islands.append(island)
    return islands

def largest_island_area(grid):
    if not grid:
        return -1
    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * cols for _ in range(rows)]
    max_area = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and not visited[r][c]:
                visited[r][c] = True
                queue = deque([(r, c)])
                area = 0
                while queue:
                    cr, cc = queue.popleft()
                    area += 1
                    for dr, dc in directions:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows\
                        and 0 <= nc < cols\
                        and grid[nr][nc] == 0\
                        and not visited[nr][nc]:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
                max_area = max(max_area, area)
    return max_area

def lee_algorithm(grid, start, end):
    if not grid:
        return -1
    rows, cols = len(grid), len(grid[0])
    sr, sc = start
    er, ec = end
    if not (0 <= sr < rows and 0 <= er < rows and 0 <= sc < cols and 0 <= ec < cols)\
    or grid[sr][sc] != 0 or grid[er][ec] != 0:
        return -1
    if start == end:
        return [start]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * cols for _ in range(rows)]
    visited[sr][sc] = True
    queue = deque([(sr, sc)])
    parent = [[None] * cols for _ in range(rows)]
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows\
            and 0 <= nc < cols\
            and not visited[nr][nc]\
            and grid[nr][nc] == 0:
                parent[nr][nc] = (r, c)
                if (nr, nc) == end:
                    path = []
                    cur = nr, nc
                    while cur != None:
                        path.append(cur)
                        cur = parent[cur[0]][cur[1]]
                    return path[::-1]
                visited[nr][nc] = True
                queue.append((nr, nc))
    return None

def lee_algorithm_len(grid, start, end):
    if not grid:
        return -1
    rows, cols = len(grid), len(grid[0])
    sr, sc = start
    er, ec = end
    if not (0 <= sr < rows and 0 <= er < rows and 0 <= sc < cols and 0 <= ec < cols)\
    or grid[sr][sc] != 0 or grid[er][ec] != 0:
        return -1
    if start == end:
        return 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * cols for _ in range(rows)]
    visited[sr][sc] = True
    queue = deque([(sr, sc, 0)])
    while queue:
        r, c, dist = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows\
            and 0 <= nc < cols\
            and not visited[nr][nc]\
            and grid[nr][nc] == 0:
                if (nr, nc) == end:
                    return dist + 1
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))
    return None

def dist_to_nearest_one(grid):
    if not grid:
        return -1
    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()
    dist = [[float('inf')] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                dist[r][c] = 0
                queue.append((r, c))
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
    return dist

def rotting_oranges(grid):
    if not grid:
        return -1
    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()
    fresh_count = 0
    max_time = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh_count += 1
    while queue:
        r, c, time = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    max_time = max(max_time, time + 1)
                    queue.append((nr, nc, time + 1))
    return max_time if fresh_count == 0 else None

def knight_moves(n, start, end):
    if n <= 0\
    or not (0 <= start[0] < n and 0 <= start[1] < n and 0 <= end[0] < n and 0 <= end[1] < n):
        return -1
    if start == end:
        return [start]
    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    visited = {start}
    queue = deque([start])
    parent = {start: None}
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                parent[(nr, nc)] = (r, c)
                if (nr, nc) == end:
                    path = []
                    cur = nr, nc
                    while cur != None:
                        path.append(cur)
                        cur = parent[cur]
                    return path[::-1]
                visited.add((nr, nc))
                queue.append((nr, nc))
    return None

def knight_moves_len(n, start, end):
    if n <= 0\
    or not (0 <= start[0] < n and 0 <= start[1] < n and 0 <= end[0] < n and 0 <= end[1] < n):
        return -1
    if start == end:
        return 0
    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    visited = {start}
    queue = deque([(start[0], start[1], 0)])
    while queue:
        r, c, dist = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                if (nr, nc) == end:
                    return dist + 1
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    return None