import sys
from collections import deque

board = [[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]
m = len(board)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
sum = 0
Q = deque()
Q.append((0, 0))
d = [[0] * m for _ in range(m)]
d
[0][0] = 1
while Q:
    tmp = Q.popleft()
    for j in range(4):
        x = tmp[0] + dx[j]
        y = tmp[1] + dy[j]
        if 0 <= x <= m and 0 <= y <= m and d[x][y] == 0:
            board[x][y] = 1
            Q.append((x, y))
