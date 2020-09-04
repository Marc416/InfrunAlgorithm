# 중복이 없는 문제 요소라면 이차원 배열을 쓴다
# 근데 너무 많이 시간이 걸리니까 끝에서 아래로 내려오게 한다
import sys

sys.stdin = open('10.txt', 'rt')
n, m = map(int, input().split())
dy = [0] * (m + 1)
for i in range(n):
    ps, pt = map(int, input().split())
    # 뒤에서 부터 탐색
    for j in range(m, pt - 1, -1):
        dy[j] = max(dy[j - pt] + ps, dy[j])

print(dy[m])
