import sys
import heapq as hq

sys.stdin = open('10.txt', 'rt')
a = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        # 입력한 수가 0이고 트리에 아무것도 없으면
        if len(a) == 0:
            print(-1)
        else:
            # 가장위의 힙을 빼서 프린트
            print(hq.heappop(a))
    else:
        # a에 n을 힙으로 넣으라
        hq.heappush(a, n)
