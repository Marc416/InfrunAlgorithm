# 이문제는 돌다리를 마지막에 건너야 하기 때문에 +1을 더해줘야하네

import sys

sys.stdin = open('03.txt', 'rt')
n = int(input())
dy = [0] * (n + 2)
dy[1] = 1
dy[2] = 2

for i in range(3, n + 2):
    # 3배수 돌다리를 못건넌다고 할 때(옵션한번 줘봄)
    if i % 3 == 0:
        continue
    dy[i] = dy[i - 2] + dy[i - 1]
print(dy[n+1])
