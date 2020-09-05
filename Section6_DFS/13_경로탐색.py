import sys

sys.stdin = open('13.txt', 'rt')
n, m = map(int, input().split())
g = [[0] * (n + 1) for _ in range(n + 1)]
ch = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1

for i in g:
    print(i)

cnt = 0


def DFS(v):
    global cnt
    if v == n:
        cnt += 1
        return
    else:
        for i in range(1, n + 1):
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                DFS(i)
                ch[i] = 0


ch[1] = 1
DFS(1)
print(cnt)
