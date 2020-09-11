import sys

sys.stdin = open('연속합.txt', 'rt')
n = int(input())
li = list(map(int, input().split()))
li.insert(0, 0)
dy = [0] * (n + 1)
dy[1] = li[1]
maxV = 0
index = 0
for i in range(2, n + 1):
    dy[i] = max(dy[i - 1] + li[i], li[i])
    if maxV < dy[i]:
        maxV = dy[i]
        index = i
print(dy)
print(i)

