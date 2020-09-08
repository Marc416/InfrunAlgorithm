import sys

sys.stdin = open('01.txt', 'rt')
w = input()


def balanced(p):
    num = 0
    temp = []
    for idx, value in enumerate(p):
        if value == ')':
            num -= 1
        if value == '(':
            num += 1
        if num == 0:
            return idx


def is_right(str):
    temp = []
    for i in str:
        if i == '(':
            temp.append(i)
        else:
            if len(temp) == 0:
                return False
            # 짝이 맞는 것이므로 빼버린다
            temp.pop()

    # temp에 뭔가 남아 있으면 짝이 안맞는 것임
    if len(temp) != 0:
        return False
    return True


if w == '' or is_right(w):
    print(w)

u, v = w[:balanced(w)+1], w[balanced(w)+1:]

if is_right(u):

if w == '':
    print(w)
