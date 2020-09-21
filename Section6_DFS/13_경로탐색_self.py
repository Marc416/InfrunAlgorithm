import sys

sys.stdin = open('13.txt', 'rt')
n, m = map(int, input().split())
g = [[0] * (n + 1) for _ in range(n + 1)]

ch = [0] * (n + 1)
for _ in range(m):
    s, e = map(int, input().split())
    g[s][e] = 1

cnt = 0


def DFS(now):
    global cnt
    if now == n:
        cnt +=1
        return
    else:
        for next in range(1, n + 1):
            if g[now][next] ==1 and ch[next] ==0:
                ch[next] = 1
                DFS(next)
                ch[next] = 0

DFS(1)
print(cnt)
