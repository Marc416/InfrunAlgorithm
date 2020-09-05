import sys

sys.stdin = open('16.txt', 'rt')
board = list(list(map(int, input().split())) for _ in range(10))
ch = list(list([0] * 10) for _ in range(10))
# 목적지로부터 거슬러 올라간다
# 목적지 찾기
for i in range(10):
    if board[9][i] == 2:
        y = i
        break


def DFS(x, y):
    ch[x][y] = 1
    if x == 0:
        print(y)
        return
    # 왼쪽 탐색, 왼쪽 벽인 0보다 크고 가본적이 없으며, 길인 곳
    if y - 1 >= 0 and ch[x][y - 1] == 0 and board[x][y - 1] == 1:
        DFS(x, y - 1)
    elif y + 1 < 10 and ch[x][y + 1] == 0 and board[x][y + 1] == 1:
        DFS(x, y + 1)
    elif x - 1 >= 0 and ch[x - 1][y] == 0 and board[x - 1][y] == 1:
        DFS(x - 1, y)


DFS(9, y)
