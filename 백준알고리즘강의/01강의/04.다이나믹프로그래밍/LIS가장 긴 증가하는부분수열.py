import sys

sys.stdin = open('LIS가장긴 증가하는 부분수열', 'rt')
n = int(input())
dy = [0] * (n + 1)
li = list(map(int, input().split()))
for i in range(n):
    dy[i] = 1
    for j in range(i):
        print(dy)
        # 기준이 되는 i숫자가 앞에있는j숫자보다 크고 i번째 숫자를 뽑는
        # 순열개수보다 앞에 있는j순열에 +1한 개수보다 작다면
        if li[i] > li[j] and dy[i] < dy[j] + 1:
            dy[i] = dy[j] + 1
print(dy)
print(dy[n - 1])
