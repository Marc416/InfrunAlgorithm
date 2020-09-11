import sys
sys.stdin = open('쉬운계단수', 'rt')
d = [[0] * 10 for _ in range(100 + 1)]
mod = 1000000000

n = int(input())
# 1의자리수는 계단이 모두 1개:
#     1,2,3,4,5,6,7,8,9,
for i in range(1, 10):
    d[1][i] = 1
# 2자리 수
for i in range(2, n + 1):
    # j숫자로 끝나는 수일 경우
    for j in range(10):
        d[i][j] = 0
        # j숫자보다 1작거나 1큰 수일 경우
        if j - 1 > 0:
            d[i][j] += d[i - 1][j - 1]
        if j + 1 <= 9:
            d[i][j] += d[i - 1][j + 1]
        d[i][j] %= mod
# 1자리 수(1,2,3,4,5,6,7,...9)일 때 계단 식으로 된 수는 몇개인가?
print(d[n])
ans = sum(d[n]) % mod
print(ans)
# https://mygumi.tistory.com/260
