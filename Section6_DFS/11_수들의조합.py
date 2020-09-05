import sys

sys.stdin = open('11.txt', 'rt')
n, k = map(int, input().split())
li = list(map(int, input().split()))
res = [0] * n
cnt = 0
m = int(input())


def DFS(L, S, sum):
    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1
            return
        return
    else:
        for i in range(S, n):
            DFS(L + 1, i + 1, sum + li[i])


DFS(0, 0, 0)
print(cnt)
