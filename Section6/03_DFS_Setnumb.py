import sys

sys.stdin = open('03.txt', 'rt')
n = int(input())
ch = [0] * (n + 1)


def DFS(v):
    # 브레이크 지점
    if v == n + 1:
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end='')
        print()
    else:
        # 왼쪽으로 탐색
        ch[v] = 1
        DFS(v + 1)
        # 오른쪽으로 탐색
        ch[v] = 0
        DFS(v + 1)


DFS(1)
