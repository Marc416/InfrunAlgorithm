import sys

sys.stdin = open('0.txt', 'rt')
a, b, c = list(int(input()) for _ in range(3))
print(a, b, c)
