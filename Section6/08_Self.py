import sys

sys.stdin = open('08.txt', 'rt')
n, m = map(int, input().split())
ch = [0] * (n + 1)


def DFS(L):
    if L == m+1:
        for i in range(1, len(ch)):
            if ch[i] == 1:
                print(i)
        print()
        return
    else:
        ch[L] = 1
        DFS(L + 1)
        ch[L] = 0
        DFS(L + 1)


DFS(1)
