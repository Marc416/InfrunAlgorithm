from collections import deque

ball = [11, 2, 9, 13, 24]
order = [9, 2, 13, 24, 11]

ballbox = deque(ball)
cnt = []
while order:
    for i in order:
        if i == ballbox[0]:
            cnt.append(ballbox.popleft())
            order.remove(i)
            break
        elif i == ballbox[-1]:
            cnt.append(ballbox.pop())
            order.remove(i)
            break

print(cnt)
