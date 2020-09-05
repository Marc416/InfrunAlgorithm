import sys

sys.stdin = open('11.txt', 'rt')
n, k = map(int, input().split())
li = list(map(int, input().split()))
res = [0] * n
cnt = 0
m = int(input())


def DFS(L, S):
    global cnt
    if L == k:
        if sum(res) % m == 0:
            print(res)
            cnt += 1
            # res.clear()
            return
        return
    else:
        for i in range(S, n):
            res.append(li[i])
            # i대신에 S를 넣어서 틀림
            # DFS(L+1, S+1)
            DFS(L+1, i+1)
            res.pop()

DFS(0, 0)
print(cnt)