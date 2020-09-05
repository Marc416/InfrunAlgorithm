import sys
from collections import deque

sys.stdin = open('05.txt', 'rt')

n, k = map(int, input().split())
# 1~n+1까지의 수로 초기화한다
dq = list(range(1, n + 1))
# dq를 큐로 자료구조를 변형
dq = deque(dq)
while dq:
    # k번째를 뺄거니까 k-1번만 반복해서 숫자 뒤로보내기
    for _ in range(k - 1):
        # dq읜 0번째를 꺼낸다
        cur = dq.popleft()
        # 뒤로 보낸다
        dq.append(cur)
    # k번째 숫자빼기
    dq.popleft()
    # dq의 수가 1개만 남을경우 정답출력
    if len(dq) == 1:
        print(dq[0])
        # 브레이크를 써도 되고 팝을 써서 while 문 종료시켜도 됨
        dq.popleft()
