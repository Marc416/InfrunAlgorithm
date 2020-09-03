# 비교해야할게 두가지라면 한가지 부분을 정렬 시켜놓고 비교
import sys

sys.stdin = open('06.txt', 'rt')
n = int(input())
brick = list(list(map(int, input().split())) for _ in range(n))
# 비교해야할 것 둘중 하나로 먼저 정렬해 준다
# 다음 인덱스로 정렬하는 방법 알아보기
brick.sort(reverse=True)
dy = [0] * n
dy[0] = brick[0][1]

res = 0
for i in range(1, n):
    maxh = 0
    # 0까지 탐색하면 인덱스 1번까지 된다, -1이라고 하면 0까지 내려올 수 있다.
    # 이유는 잘 모르겠음
    for j in range(i - 1, -1, -1):
        # 다음게 넓이가 더 좁고 , 무게가 더 가벼우면
        if brick[j][2] > brick[i][2] and dy[j] > maxh:
            maxh = dy[j]
        dy[i] = maxh + brick[i][1]
        res = max(res, dy[i])
print(res)
