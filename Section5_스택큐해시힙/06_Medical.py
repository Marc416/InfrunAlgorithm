import sys
from collections import deque

sys.stdin = open('06.txt', 'rt')

n, m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt = 0
while True:
    cur = Q.popleft()
    # 큐에서 0번째 수를  cur에 넣어서 꺼내 놓고
    # Q에 아직 남아 있는 수들을 비교한다. 인덱스가 1인이유는
    # 현재 튜플로(idx, val)형식으로 되어 있어서그렇다
    # any라는 함수는 단한개라도 이러한 조건이 있을 경우 true
    if any(cur[1] < x[1] for x in Q):
        Q.append(cur)
    # 단한개도 위의 식이 참이 아닐경우 즉 가장 위험도가 높은 경우
    else:
        # 몇번째 진료인지 체크
        cnt += 1
        # m번째 사람이 진료받는 번째는 몇번째인가?
        if cur[0] == m:
            print(cnt)
            break
