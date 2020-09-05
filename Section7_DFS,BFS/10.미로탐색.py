import sys
from collections import deque

sys.stdin = open('10.txt', 'rt')
board = [list(map(int, input().split())) for _ in range(7)]
board[0][0]=1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0


def DFS(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
        return
    else:
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a <= 6 and 0 <= b <= 6 and board[a][b] == 0:
                    board[a][b] = 1
                    DFS(a, b)
                    board[a][b] = 0


DFS(0, 0)
print(cnt)
