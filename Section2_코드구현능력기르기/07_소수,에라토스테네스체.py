import sys

sys.stdin = open("07.txt", "r")
n = int(input())
ch = [0] * (n + 1)
cnt = 0
for i in range(2, n + 1):
    if ch[i] == 0:
        # 모든 수에 처음에 1을 더한다
        cnt += 1
        # i로 나누어지는 배수들을 모두 배제 시킨다
        for j in range(i, n + 1, i):  # i부터 n+1까지 i만큼 증가시킨 인덱스에 접근
            ch[j] = 1
print(cnt)
