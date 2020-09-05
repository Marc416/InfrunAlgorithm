import sys

sys.stdin = open('02.txt', 'rt')
n = int(input())
T = list()
P = list()
res = 0
for i in range(n):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)
T.insert(0, 0)
P.insert(0, 0)


def DFS(L, sum):
    global res
    if L == n + 1:
        if sum > res:
            res = sum
        return
    else:
        if L + T[L] <= n + 1:
            DFS(L + T[L], sum + P[L])
        DFS(L + 1, sum)


DFS(1, 0)
print(res)
