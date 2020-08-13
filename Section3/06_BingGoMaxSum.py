import sys

sys.stdin = open('06.txt', 'rt')

n = int(input())

li = []
for i in range(n):
    li.append(list(map(int, input().split())))

largest = -21470000
# 가로 세로 합중 가장 큰것을 Largest에 저장
for i in range(n):
    # 가로합, 세로합
    crossSum = columnSum = 0
    for j in range(n):
        crossSum += li[i][j]
        columnSum += li[j][i]

    if crossSum > largest:
        largest = crossSum
    if columnSum > largest:
        largest = columnSum

# 대각선 중 가장큰것을 비교해서 Largest에 저장

slsh = rvsslsh=0
for i in range(n):
    slsh += li[i][i]
    rvsslsh += li[i][n-i-1]

if slsh > largest:
    largest = slsh
if rvsslsh > largest:
    largest = rvsslsh

print(largest)
