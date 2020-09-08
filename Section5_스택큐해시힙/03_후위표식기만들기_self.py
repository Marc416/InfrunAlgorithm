import sys

sys.stdin = open('03.txt', 'rt')
a = input()
stack = []
res = ''
for i in a:
    if i.isdecimal():
        res +=i
    else:
        if i == '(':

        elif i == '*' or i == '/':
        elif i == '+' or i == '-':
            res += i