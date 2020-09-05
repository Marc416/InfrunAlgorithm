import sys
# 개어려웠음..

sys.stdin = open('05.txt', 'rt')

n, m = map(int, input().split())
a = list(map(int, input().split()))

lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    # 합을 기준으로 크냐 작냐 같냐에 따라 flag의 위치를 옮긴다
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
        print(lt, rt)
    else:
        tot -= a[lt]
        lt += 1

print(cnt)
