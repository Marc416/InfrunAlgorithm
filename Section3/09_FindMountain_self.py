import sys
from builtins import list

sys.stdin = open('09.txt', 'rt')

n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))

for i in range(n):
    li[i].append(0)
    li[i].insert(0, 0)

zeroLi = []
for _ in range(n + 2):
    zeroLi.append(0)
li.append(zeroLi)
li.insert(0, zeroLi)

cnt = 0
for i in range(n):
    for j in range(n):
        # 왼, 오, 위, 아래
        if li[i + 1][j + 1] > li[i][j + 1] \
                and li[i + 1][j + 1] > li[i + 2][j + 1] \
                and li[i + 1][j + 1] > li[i + 1][j] \
                and li[i + 1][j + 1] > li[i + 1][j + 2]:
            cnt += 1

print(cnt)
