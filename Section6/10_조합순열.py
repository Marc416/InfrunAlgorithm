import sys

sys.stdin = open('10.txt', 'rt')
n, m = map(int, input().split())

res = [0] * (n + 1)


def DFS(L, s):
    if L == m:
        for i in range(len(res)):
            if res[i] == 1:
                print(i, end= ' ')
        print()
        return
    else:
        for i in range(s, n + 1):
            res[i] = 1
            DFS(L+1, i + 1)
            res[i] = 0


DFS(0, 1)
