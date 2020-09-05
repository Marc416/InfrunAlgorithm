import sys

sys.stdin = open('09.txt', 'rt')

n = int(input())
li = list(map(int, input().split()))

numb = 0
pos = []

while li:
    if len(li) == 1 and li[0]>numb:
        pos.append('L')
    if li[0] > numb:
        numb = li[0]
        li.pop(0)
        pos.append('L')

    elif li[0] <= numb:
        li.pop(0)
    elif li[-1] > numb:
        numb = li[-1]
        li.pop()
        pos.append('R')
    elif li[-1] <= numb:
        li.pop()

print(len(pos))
for i in pos:
    print(i, end='')
 

