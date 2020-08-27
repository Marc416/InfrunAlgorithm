import sys

sys.stdin = open('01.txt', 'rt')
a, b, c = list(int(input()) for i in range(3))
print(a, b, c)
mul = a * b * c
li = [0] * 10
# -----------------------------------
# 다른 부분
while mul > 0:
    divide = mul % 10
    mul = mul // 10
    li[divide] += 1

# -----------------------------------
# 공통
for i in li:
    print(i)
