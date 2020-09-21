import sys

INF = sys.maxsize
sys.stdin = open('종만복재귀연습.txt', 'rt')
n = int(input())

path = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]
ch = [0] * n
res = INF


def DFS(l, s, now, d):
    global res
    if l == n:
        res = min(res, d)
        # print(d)
        return
    else:
        for i in range(n):
            if ch[i] == 1 or path[now][i] == 0:
                continue
            else:
                ch[i] = 1
                DFS(l + 1, s, i, d + path[now][i])
                ch[i] = 0


for i in range(n):
    DFS(0, i, i, 0)
print(res)
