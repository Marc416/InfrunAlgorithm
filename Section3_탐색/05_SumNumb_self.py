import sys

# 개어려웠음..

sys.stdin = open('05.txt', 'rt')

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.insert(n,0)
print(a)

tot = 0
lt = 0
cnt = 0

while lt < n:
    tot = a[lt]
    for i in range(lt + 1, n+1):
        tot += a[i]
        if tot == m:
            cnt += 1
            lt += 1
            break
        elif tot > m:
            lt += 1
            break
    lt +=1

print(cnt)
