import sys

sys.stdin = open('01.txt', 'rt')

n = int(input())


def DFS(a):
    if a == 0:
        return
    else:
        DFS(a // 2)
        print(a % 2, end='')

