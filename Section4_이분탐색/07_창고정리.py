import sys

sys.stdin = open('07.txt', 'rt')
L = int(input())
a = list(map(int, input().split()))
m = int(input())
a.sort()
# 있는 그대로 구현시키기
for _ in range(m):
    a[0] += 1
    a[L - 1] -= 1
    a.sort()

print(a[L - 1] - a[0])
