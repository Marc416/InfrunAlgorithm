import sys

sys.stdin = open('02.txt', 'rt')

s = input()
li = []
cnt = 0
for i in range(len(s)):

    if s[i] == '(':
        li.append(s[i])
    else:
        if li[-1] == '(':
            li.pop()
            cnt +=len(li)
        else:
            li.pop()
            cnt+=1

print(cnt)