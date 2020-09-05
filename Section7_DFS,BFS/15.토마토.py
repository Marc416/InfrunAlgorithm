import sys
from collections import deque

sys.stdin = open('15.txt', 'rt')
m, n = map(int, input().split())
box = list(list(map(int, input().split())) for _ in range(n))
dis = list([0] * m for _ in range(n))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 최소 몇일이 지나야 다 익는가

Q = deque()
res = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            Q.append((i, j))
while Q:
    tmp = Q.popleft()
    for a in range(4):
        x = tmp[0] + dx[a]
        y = tmp[1] + dy[a]
        if 0 <= x < n and 0 <= y < m and box[x][y] == 0:
            box[x][y] = 1
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            Q.append((x, y))
    for i in range(n):
        print(dis[i])
    print()

flag = 1
for i in range(n):
    for j in range(m):
        # 익을 토마토가 1개라도 있다면
        if box[i][j] == 0:
            flag = 0
            # 아하! BFS로 토마토 다 익혀 놨기 때문에 0으로 안익은 애들이 없겠구먼
            # -1로 뒤덮여있어서 못익는 토마토가 있을 수도 있기 때문에 하는 플래그임
            print('플래그',flag)
            
# 토마토가 익는데에 걸리는 최대 값
if flag == 1:
    for i in range(n):
        for j in range(m):
            res = max(dis[i][j], res)
    # 아 토마토가 전부 익으면 익을 토마토가 없기 때문에 0일이구나 결국 0이 나옴
    print('res:', res)
else:
    print(-1)

