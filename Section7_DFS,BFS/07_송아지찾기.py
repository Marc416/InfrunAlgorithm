import sys
from collections import deque
sys.stdin = open('07.txt', 'rt')
# BFS는 출발점에서 최단거리로 가는게 무엇인지 찾는것
# 좌표는 최대 10000까지
MAX = 10000
# 체크 지점 위치
ch = [0]*(MAX+1)
# 거리
dis = [0]*(MAX+1)
n, m = map(int, input().split())
# 처음 시작위치 표시
ch[n]=1
# 시작부터 n까지의 거리표시
dis[n]=0
dQ = deque()
dQ.append(n)
while dQ:
    now = dQ.popleft()
    # 도착지점 발견하면 정지
    if now == m:
        break
    # 시작지점 -1, 시작지점 +1, 시작지점 +5를방문한다
    for next in(now-1, now+1, now+5):
        # 좌표는 0보다 커야한다 조건에 나옴
        if 0 < next <= MAX:
            # next에 방문을 했다면 return
            # 방문안한거만 체크
            if ch[next] == 0:
                dQ.append(next)
                ch[next]=1
                # 시작지점부터 dis[x]의 도착지점까지로 가는데 걸리는 순회 카운트를 나타냄
                # 그래서 이전 위치에서의 카운트 +1을 하는 것임
                dis[next]=dis[now]+1
print(dis[m])

