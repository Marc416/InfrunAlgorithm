import sys

sys.stdin = open('08.txt', 'rt')
n, m = map(int, input().split())
li = list(list(map(int, input().split())) for _ in range(n))
# 두번째 원소를 기준으로 다차원배열 정렬
li.sort(key=lambda x: x[1], reverse=True)
ch = [0] * n
# 가치
ch[0] = li[0][1]
# 무게
kg = li[0][0]
for i in range(1, n):
    if kg + li[i][0] < m:
        ch[i] = ch[i - 1] + li[i][1]
        kg += li[i][0]
