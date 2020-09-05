# 피자집을 찾는다
# 집을 찾는다
# 거리를 잰다
import sys
from collections import deque

sys.stdin = open('17.txt', 'rt')
n, m = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))

# 가게
sQ = deque()
# 집
hQ = deque()

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            sQ.append((i, j))
        elif board[i][j] == 1:
            hQ.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = 0
shopCnt = len(sQ)
for _ in range(shopCnt):
    ch = list([0] * n for _ in range(n))
    cnt = 0
    while sQ:
        tmp = sQ.popleft()
        if ch[tmp[0]][tmp[1]] > 4:
            res -= ch[tmp[0]][tmp[1]]
            break

        if board[tmp[0]][tmp[1]] == 1:
            res += ch[tmp[0]][tmp[1]]
            break
        for i in range(4):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            if 0 <= x < n and 0 <= y < n and ch[x][y] == 0:
                ch[x][y] = ch[tmp[0]][tmp[1]] + 1
                sQ.append((x, y))

print(res)