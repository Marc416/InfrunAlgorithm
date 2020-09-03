# 이문제는 돌다리를 마지막에 건너야 하기 때문에 +1을 더해줘야하네

import sys
from collections import deque

sys.stdin = open('04.txt', 'rt')
n = int(input())
li = deque(map(int, input().split()))
# 인덱스 셋팅을 배열과 맞추기위해 0인덱스에 0추가
li.insert(0, 0)

dy = [0] * (n + 1)
dy[1] = 1
res = 0

for i in range(2, n + 1):
    max = 0
    # i번째 바로 앞에서 0번까지 거꾸로 탐색 -1씩 줄인다
    for j in range(i - 1, 0, -1):
        if li[j] < li[i] and dy[j] > max:
            max = dy[j]
    dy[i] = max + 1
    # 최대길이 설정
    if dy[i] > res:
        res = dy[i]
print(res)
