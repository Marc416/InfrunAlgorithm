# 이문제를 풀지 못한 이유.
# 1. 0~100까지의 높이를 모두 검색을 해야 하는 줄 몰랐다
# -> 이해에 대한 오류
# 2. 문제를 2개풀고 지쳐서 더이상 풀고 싶어지지 않아서 금방 포기했다
# -> 앞으로 시간 리미트를 두고 꼭 해당 시간 동안 풀아보는 옂습을 할 것
import sys
from collections import deque
# 재귀를 제한 시켜줘야 한다. 재귀 쓸 때 시간 리미트를 걸어 주기
sys.setrecursionlimit(10**6)

sys.stdin = open('14.txt', 'rt')
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
Q = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
res = 0


def DFS(x, y, h):
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > h:
            DFS(xx, yy, h)


# 높이가 0~100까지 탐색을 할 때마다 ch리셋
# 간과한게 있는데 높이가 낮으면 물에 다 잠기니까 안전영역이 많을거라 생각했다
# 그런데 만약에 0이나 1일 경우 맵 전체가 안전영역이기 때문에 이걸 각각 하나씩
# 보는 것이 아니고 통째로 1개로 봐야함.
for h in range(100):
    # 왜 체크 리스트를 만들었을까
    ch = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            # 체크리스트에 체크가 안되어 있고 h보다 높이가 높다면
            if ch[i][j] == 0 and board[i][j] > h:
                cnt += 1
                DFS(i, j, h)


    res = max(res, cnt)

    # 높이 디버깅
    print(h, '높이', '안전지역 수 :',cnt)
    for a in range(n):
        print(ch[a])
    print()
    # 높이디버깅

    # 다 돌았음에도 cnt가 0이라는 것은 Max높이 이후의 것임! 이것들은 체크할 필요없음
    # 전부 물에 잠길것임
    if cnt == 0:
        break
print(res)
