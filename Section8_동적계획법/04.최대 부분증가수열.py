# 이문제는 돌다리를 마지막에 건너야 하기 때문에 +1을 더해줘야하네

import sys
from collections import deque

sys.stdin = open('04.txt', 'rt')
n = int(input())
li = deque(map(int, input().split()))
ch = []

# li = list(map(int, input().split()))
# a를 체크리스트 인덱스 1에 넣는다
# b가 i-1보다 크면 체크리스트 i 리스트에 넣는다
# 이건 앞에 두개이상 있을 때로 제한
# b가 i-1보다 작고 && i-2보다 작으면 다음껄 검색한다
# 그렇지 않으면 pop하고 append하라
i = 0
ch.append(li.popleft())
while i < n:
    if ch[i] < li[0]:
        ch.append(li.popleft())
        i += 1
    elif i >= 2:
        if ch[i - 1] > li[0]:
            li.popleft()
            continue
        elif ch[-1] < li[0]:
            ch.append(li.popleft())
            i += 1

print(ch)
