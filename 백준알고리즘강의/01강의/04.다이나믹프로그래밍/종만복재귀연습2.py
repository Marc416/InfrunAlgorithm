import sys

sys.stdin = open('종만복재귀연습.txt', 'rt')
n = int(input())

path = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]
visit = [0] * n
res = 16780000


def shortCut(l, t):
    global res
    if l < n:
        print('a',t)
        return t

    for i in range(n):
        for j in range(n):
            if visit[i] > 0 and i == j:
                continue
            else:
                visit[i] = 1
                t = t + shortCut(l+1, path[l][i])
                visit[i] = 0



shortCut(0, 0)

print(res)
