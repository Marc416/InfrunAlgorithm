import sys

sys.stdin = open('01.txt', 'rt')
n, m = map(int, input().split())
ch = [0] * n
g = [list(map(int, input().split())) for _ in range(1, n + 1)]
cnt = 0
print(g)


def DFS(l, t):
    global cnt
    if t > m:
        cnt += 1
        print(t)
        return
    else:
        t += g[l][1]
        ch[l] = 1
        for i in range(n):
            if ch[i] != 1:
                DFS(i, t)
    print()


DFS(0, 0)
