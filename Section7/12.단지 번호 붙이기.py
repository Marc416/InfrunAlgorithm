import sys

sys.stdin = open('12.txt', 'rt')
n = int(input())
board = list(list(map(int, input())) for _ in range(n))
vil = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global cnt
    cnt += 1
    board[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
            DFS(nx, ny)


res = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt = 0
            DFS(i, j)
            res.append(cnt)

print(len(res))
res.sort()
print(res)