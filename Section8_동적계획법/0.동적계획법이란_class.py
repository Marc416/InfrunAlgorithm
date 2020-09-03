# 동적 계획법이란 ?
# 작은 문제로 규칙을 만들어 푸는 것, 점화식
# DP인지 아는 방법은? 중복되는 규칙이 보인다?
import sys

sys.stdin = open('0.txt', 'rt')
n = int(input())
dy = [0] * (n + 1)
# 직관적으로 알만한 것은 초기화 한다
dy[1] = 1
dy[2] = 2
for i in range(3, n + 1):
    dy[i] = dy[i - 1] + dy[i - 2]

print(dy[7])
