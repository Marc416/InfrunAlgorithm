board = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
r = 1
c = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
for i in board:
    for j in i:
        if i > 0:
            cnt += 1
cnt = cnt // 2


def DFS(l, r, c):
    if l
