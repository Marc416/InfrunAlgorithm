import sys

sys.stdin = open('06.txt', 'rt')

n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))

li.sort(reverse=True)

weight = 0
height = 0
cnt = 0
print(li)
for i in li:
    if height < i[0] or weight < i[1]:
        print('i' , i[0], i[1], end= ' ')
        print('기록' , height, weight)
        cnt += 1
        height = i[0]
        weight = i[1]

print(cnt)
