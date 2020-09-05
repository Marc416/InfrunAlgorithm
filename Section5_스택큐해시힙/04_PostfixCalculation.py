import sys

sys.stdin = open('04.txt', 'rt')

stack = []
a = input()
res = 0
for i in a:
    if i.isdecimal():
        stack.append(int(i))
    elif i == '+':
        res = stack.pop(-2) + stack.pop()
        stack.append(res)
    elif i == '*':
        res = stack.pop(-2) * stack.pop()
        stack.append(res)
    elif i == '/':
        res = stack.pop(-2) / stack.pop()
        stack.append(res)
    elif i == '-':
        res = stack.pop(-2) - stack.pop()
        stack.append(res)

print(stack[0])
