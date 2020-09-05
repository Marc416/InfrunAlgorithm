import sys

sys.stdin = open('04.txt', 'rt')
n, c = map(int, input().split())
line = []
for _ in range(n):
    tmp = int(input())
    line.append(tmp)

line.sort()


def Count(length):
    cnt = 1
    # 첫번째말 배치
    ep = line[0]
    for i in range(1, n):
        if line[i] - ep >= length:
            cnt += 1
            ep = line[i]
    return cnt


lt = 1
rt = line[n - 1]
while lt <= rt:
    mid = (lt + rt) // 2
    if Count[mid] >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
