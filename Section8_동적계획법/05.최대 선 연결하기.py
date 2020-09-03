import sys

sys.stdin = open('05.txt', 'rt')
n = int(input())
li = list(map(int, input().split()))
li.insert(0, 0)
dy = [0] * (n + 1)
dy[1] = 1
# sid = 1
res = 0

for i in range(2, n + 1):
    Maxlngth = 0
    for j in range(i - 1, 0, -1):
        if li[j] < li[i] and dy[j] > Maxlngth:
            Maxlngth = dy[j]
            print(li[j], end=' ')
    print()
    dy[i] = Maxlngth + 1

    # if i == li[j]:
    #     sid = j
    #     lngth += 1
    #     dy[i] = lngth
    #     break
    # dy[i] = res

    res = max(res, dy[i])

print(res)
