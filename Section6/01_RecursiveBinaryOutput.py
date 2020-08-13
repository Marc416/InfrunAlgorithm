import sys

sys.stdin = open('01.txt', 'rt')
n = int(input())


def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x%2, end='')

DFS(n)
