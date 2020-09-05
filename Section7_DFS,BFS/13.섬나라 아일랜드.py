import sys
from collections import deque

sys.stdin = open('13.txt', 'rt')
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
cnt = 0
Q = deque()

for i in range(n):
    print('행',i)
    for j in range(n):
        print(i, j, end='')
        print()
        if board[i][j] == 1:
            board[i][j] = 4
            Q.append((i, j))
            while Q:
                tmp = Q.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0 <= x < n and 0 <= y < n and board[x][y] == 1:
                        board[x][y] = 0
                        Q.append((x, y))
                        for a in range(n):
                            print(board[a])
                        print()
            print('하나 끝남')
            cnt += 1

print(cnt)
