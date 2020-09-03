import sys

sys.stdin = open('0.txt', 'rt')
n = int(input())

li = []

cnt = 0


def DFS(sum):
    global cnt

    if sum > n:
        return
    if sum == n:
        cnt += 1
        return

    else:
        for i in range(1, 3):
            sum += i
            DFS(sum)
            sum -= i


DFS(0)
print(cnt)
