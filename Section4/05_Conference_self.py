import sys

sys.stdin = open('05.txt', 'rt')

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, len(time)):
    temp = time[i - 1]
    if time[i - 1][1] > time[i][1]:
        time[i - 1] = time[i]
        time[i] = temp

print(time)

# cnt = 0
# 처음 회의는 할거니까 카운트 1로 해줘야 하네.. 이거차이였음
cnt =1
temp = time[0]
for i in range(1, n):
    if temp[1] <= time[i][0]:
        temp = time[i]
        cnt += 1
    else:
        continue
print(cnt)
