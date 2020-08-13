import sys

sys.stdin = open('03.txt', 'rt')
a = input()
stack = []
res = ''
for x in a:
    # 피연산자일경우
    if x.isdecimal():
        res += x
    # 연산자일경우
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                # 끄집어내고 res에 넣기
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()
print(res)
