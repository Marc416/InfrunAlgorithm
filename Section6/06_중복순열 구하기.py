import sys

sys.stdin = open('06.txt', 'rt')
n, m = map(int, input().split())
res = [0]*n
# for i in range(1, n + 1):
#     res.append(i)


def DFS(L):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            res[L] = i
            DFS(L + 1)


cnt = 0
DFS(0)
