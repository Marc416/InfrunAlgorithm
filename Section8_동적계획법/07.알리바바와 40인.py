import sys

sys.stdin = open('07.txt', 'rt')
n = int(input())
li = list(list(map(int, input().split())) for _ in range(n))
ch = [[0] * (n) for _ in range(n)]
ch[0][0] = li[0][0]
for i in range(1, n):
    # 가로줄 기본 셋팅
    ch[0][i] = ch[0][i-1] + li[0][i]
    # 세로줄 셋팅
    ch[i][0] = ch[i-1][0] + li[i][0]

for i in range(1, n):
    for j in range(1, n):
        ch[i][j] = min(ch[i-1][j], ch[i][j-1]) + li[i][j]

for i in range(n):
    print(ch[i])

print(ch[n-1][n-1])

