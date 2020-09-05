import sys

sys.stdin = open('11.txt', 'rt')
n, m = map(int, input().split())
# 최소값을 구하기 위해 최대 값으로 셋팅해준다[이부분이 dp]
dis = [[5000] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    # 대각선 자기 자신을 거칠 때 비용 0
    dis[i][i] = 0
#     주어진 경로를 dis에 셋팅
for i in range(m):
    a, b, c = map(int, input().split())
    dis[a][b] = c

# 이부분이 플로이드 워샬 알고리즘 3중포문
# i에서 j로갈 때 최소비용찾기
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # k경로를 거쳤을 때의 최소 비용
            # 자기 자신경로를 지나는 비용이 0임
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dis[i][j] == 5000:
            print('M', end=' ')
        else:
            print(dis[i][j], end=' ')
    print()
