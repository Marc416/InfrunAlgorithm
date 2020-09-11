import sys
sys.stdin = open('2xn타일링', 'rt')
n = int(input())
print(n)
dy = [0]*(n+1)
dy[1] = 1
dy[2] = 2
for i in range(3, n+1):
    dy[i] = dy[i-2] + dy[i-1]
print(dy[n])