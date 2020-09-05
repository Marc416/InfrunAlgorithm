import sys

sys.stdin = open('04.txt', 'rt')
T = int(input())
k = int(input())
# coin value
cv = []
# coin n 수
cn = []
for _ in range(k):
    a, b = map(int, input().split())
    cv.append(a)
    cn.append(b)

cnt = 0


def DFS(L, sum):
    global cnt
    if sum > T:
        return
    if L == k:
        if T == sum:
            cnt += 1
            return
        else:
            return
    else:
        for i in range(cn[L] + 1):
            DFS(L + 1, sum + cv[L] * i)

DFS(0,0)
print(cnt)
