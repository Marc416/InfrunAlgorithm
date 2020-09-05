import sys

sys.stdin = open('11.txt', 'rt')
n = int(input())
sp = 124700000
ep = -124700000
initX = 0
initY = 0

mt = []
for i in range(n):
    tmp = list(map(int, input().split()))
    mt.append(tmp)
    for j in range(n):
        if mt[i][j] < sp:
            sp = mt[i][j]
            initX = i
            initY = j
        if mt[i][j] > ep:
            ep = mt[i][j]

ch = [[0] * n for _ in range(n)]
ch[initX][initY] = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0


def DFS(x, y):
    global cnt
    st = mt[x][y]
    if st == ep:
        cnt += 1
        return
    else:
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            if 0 <= nextX < n and 0 <= nextY < n and ch[nextX][nextY] == 0:
                if st < mt[nextX][nextY]:
                    ch[nextX][nextY] = 1
                    DFS(nextX, nextY)
                    ch[nextX][nextY] = 0


DFS(initX, initY)
print(cnt)
