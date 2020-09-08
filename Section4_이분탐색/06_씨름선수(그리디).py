import sys

sys.stdin = open('06.txt', 'rt')
n = int(input())
body = []
for i in range(n):
    a, b = map(int, input().split())
    body.append((a, b))
body.sort(reverse=True)
print(body)
largest = 0
cnt = 0
for x, y in body:
    # 키순으로 미리 내림차순정렬을 했기 때문에
    # 몸무게를 위에서 부터 내려가면서 무거운 순대로 넣어주면 된다
    if y > largest:
        largest = y
        cnt += 1
print(cnt)
