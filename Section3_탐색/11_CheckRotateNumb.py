import sys

sys.stdin = open('11.txt', 'rt')
li = [list(map(int, input().split())) for _ in range(7)]

cnt = 0

for i in range(3):
    for j in range(7):
        tmp = li[j][i:i + 5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if li[i + k][j] != li[i + 5 - k - 1][j]:
                break
        else:
            cnt += 1
