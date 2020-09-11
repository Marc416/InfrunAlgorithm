import sys

sys.setrecursionlimit(10000000)


def go(n):
    if n == 1:
        return 0
    if d[n] > 0:
        return d[n]
    d[n] = go(n - 1) + 1
    if n % 2 == 0:
        temp = go(n // 2) + 1
        if d[n] > temp:
            d[n] = temp
    if n % 3 == 0:
        temp = go(n // 3) + 1
        if d[n] > temp:
            d[n] = temp
    return d[n]


sys.stdin = open('1로만들기.txt', 'rt')
n = int(input())
d = [0] * (n + 1)
print(go(n))
