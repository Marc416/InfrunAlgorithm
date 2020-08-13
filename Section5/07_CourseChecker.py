import sys
from collections import deque

sys.stdin = open('07.txt', 'rt')

need = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" % (i + 1))
                break
    else:
        if len(dq) == 0:
            print('#%d YES' % (i + 1))
