import sys

sys.stdin = open('07.txt', 'rt')

l = int(input())
li = list(map(int, input().split()))
m = int(input())

li.sort(reverse=True)

top = 0
bottom = l - 1
mCount = 0
while mCount == 50:
    if li[top] > li[top + 1]:
        if li[bottom] < li[bottom - 1]:
            li[top] -= 1
            li[bottom] += 1
            mCount += 1
        else:
            bottom -= 1

    else:
        top += 1
else:
    print(li[top] - li[bottom])
