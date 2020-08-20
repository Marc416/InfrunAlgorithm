import sys

sys.stdin = open('08.txt', 'rt')


def DFS(L):
    if L == m:
        global cnt
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L + 1)
                ch[i] = 0


n, m = map(int, input().split())
res = [0] * n
ch = [0] * (n + 1)
cnt = 0
DFS(0)
print(cnt)
