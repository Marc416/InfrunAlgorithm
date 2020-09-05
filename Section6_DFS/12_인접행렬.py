import sys
sys.stdin = open('12.txt', 'rt')
n, m = map(int, input().split())
g = list([0]*(n+1) for _ in range(n+1))

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()