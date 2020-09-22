infix = ['(', '2', '+', '3', ')', '*', '4', '-', '5']
# 숫자를 먼저 넣되 전체적인 연산 순
postfix = []
# 연산자
stack = []
operator = ['*', '/', '+', '-']
bracket = ['(', ')']


def pref(x):
    if x == '*' or x == '/':
        return 2
    elif x == '+' or x == '-':
        return 1
    elif x == '(' or x == ')':
        return 0


for i in infix:
    print('i:', i)
    # 숫자인가?
    if i.isdigit() == True:
        # 숫자의 리스트에 푸시
        postfix.append(i)
    # 연산자인가?
    elif i in operator:
        # 어떤 연산자 인지 체크
        p = pref(i)
        # 스택에 다른 연산자가 있는지
        while len(stack) > 0:
            # 이미 스택에 쌓인 연산자 중 가장 먼저 연산해야 하는것을 체크
            top = stack[-1]
            print('top:', top)
            # p는 지금 현재 연산자
            print('p:', p)
            # 현재 연산자가 우선자순위가 스택에 쌓인 연산자보다 높거나 같으면
            # 괄호제외
            if pref(top) <= p:
                break
            # 현재 연산자가 연산순위가 낮으면
            postfix.append(stack.pop())
            print('postfix:', postfix)
        stack.append(i)
        print('stack:', stack)
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while True:
            x = stack.pop()
            if x == '(':
                break
            postfix.append(x)
while len(stack) > 0:
    postfix.append(stack.pop())

print(postfix)
