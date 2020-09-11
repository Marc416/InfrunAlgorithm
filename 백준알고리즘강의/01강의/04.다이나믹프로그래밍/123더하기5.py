import sys
sys.stdin = open('123더하기5.txt', 'rt')

limit = 100000
d = [[0] * 4 for _ in range(limit + 1)]
mod = 1000000009
for i in range(1, limit + 1):
    if i - 1 >= 0:
        d[i][1] = d[i - 1][2] + d[i - 1][3]
        if i == 1:
            d[i][1] = 1
    if i - 2 >= 0:
        d[i][2] = d[i - 2][1] + d[i - 2][3]
        if i == 2:
            d[i][2] = 1
    if i - 3 >= 0:
        d[i][3] = d[i - 3][1] + d[i - 3][2]
        if i == 3:
            d[i][3] = 1
    # mod로 미리 나누고 마지막에 합친 것을 다시 mod로 나누는것은
    # 원 숫자를 합쳐서 mod로 나눈 나머지의 값과 같다
    d[i][1] %= mod
    d[i][2] %= mod
    d[i][3] %= mod

t = int(input())
for _ in range(t):
    n = int(input())
    print(sum(d[n]) % mod)
