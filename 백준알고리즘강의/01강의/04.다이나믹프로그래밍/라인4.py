from collections import deque
maze = [[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]
m = len(maze)
q = deque()
check = [[False] * m for _ in range(maze)]
dist = [[0] * m for _ in range(maze)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 시작점
q.append((0, 0))
check[0][0] = True
dist[0][0] = 1

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < maze and 0 <= ny < m:
            if check[nx][ny] == False and maze[nx][ny] == 1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
                check[nx][ny] = True

print(dist[maze - 1][m - 1])