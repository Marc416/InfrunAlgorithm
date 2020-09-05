import sys

sys.stdin = open('02.txt', 'rt')


def DFS(L):
    if L > 7:
        print()
        return
    else:
        print(L, end=' ')
        DFS(L*2)
        DFS(L*2+1)


DFS(1)
