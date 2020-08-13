import sys
# from builtins import list

sys.stdin = open('09.txt', 'rt')
# 상하좌우를 탐색하기위한 셋팅
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# 위아래를 0으로 셋팅

a.insert(0, [0] * n)
a.append([0] * n)

for x in a:
    x.insert(0, 0)
    x.append(0)
cnt = 0

# 가장자리의 0구간을 지나기 위해서 1부터시작
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 파이썬에서는 all이라는 함수로 안에있는 모든 조건이 맞으면 true를 반환
        if all(a[i][j] > a[i + dx[k]][j + dy[k]] for k in range(4)):
            cnt += 1

print(cnt)
