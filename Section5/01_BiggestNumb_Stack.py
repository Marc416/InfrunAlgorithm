import sys

sys.stdin = open('01.txt', 'rt')
num, m = map(int, input().split())

num = list(map(int, str(num)))

stack = []

for x in num:
    # stack만 쓸 경우 스택이 비어있지 않으면 트루라는거임
    # 제거할숫자의 수를 기준으로한다. 왜냐하면 뺄 수 있는 수의 카운트가 정해져있다.
    # 스택에 쌓여야 뺄게 있음.
    # 마지막의 수와 현재의 수를 비교한다
    # Pop을 하면 마지막의 수를 계속 비교할 수 있다.
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1

    stack.append(x)

# 9977252641 예시에서 -3번이 x일경우 stack[-1]의 수가 x보다 크기때문에
# 팝되지 않고 m도 줄지 않는다.
# 그래서 m개의 수만큼 스택에서 빼줘야 한다.
if m != 0:
    stack = stack[:-m]

res = ''.join(map(str, stack))

print(res)
