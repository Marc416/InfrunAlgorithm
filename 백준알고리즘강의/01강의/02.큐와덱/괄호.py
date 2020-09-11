import sys

sys.stdin = open('괄호.txt', 'rt')

n = int(input())
for i in range(n):
    t = input()
    li = []
    for j in t:
        if j == '(':
            li.append(j)
        else:
            if len(li) > 0:
                if li[-1] == '(':
                    li.pop()
            else:
                li.append(j)
                break

    if len(li) != 0:
        print('NO')
    else:
        print('YES')
