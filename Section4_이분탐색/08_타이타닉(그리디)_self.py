import sys

sys.stdin = open('08.txt', 'rt')

n, m = map(int, input().split())
kg = list(map(int, input().split()))
kg.sort()
cnt = 0
# 두명이하이기 때문에 이공식이 나오는 것이구먼.. 두명 이상이면
# 많이달라지것어
lt = 0
sum = 0

# print(sum+kg[lt])
# print(m)
while kg:
    if sum + kg[lt] < m:
        sum += kg[lt]
        lt += 1
    else:
        sum = kg[lt]
        cnt += 1
        lt = 0
    kg.pop(0)
print(cnt)
