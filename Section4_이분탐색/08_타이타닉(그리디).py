import sys

sys.stdin = open('08.txt', 'rt')

n, m = map(int, input().split())
kg = list(map(int, input().split()))
kg.sort()
cnt = 0
# 두명이하이기 때문에 이공식이 나오는 것이구먼.. 두명 이상이면
# 많이달라지것어

# kg라는 자료구조가 비어있으면 멈춘다라는 뜻
while kg:
    if len(kg) == 1:
        cnt += 1
        break
    # 2명일경우
    if kg[0] + kg[-1] <= m:
        cnt += 1
        kg.pop()
        kg.pop(0)
    # 1명일경우
    else:
        cnt += 1
        kg.pop()
print(cnt)
