# 최소값을 찾는 것이므로 dy에는 큰값으로 저장이 되어야 한다
# 가방문제와 같으나 최대값이냐 최소값이냐에 따라 다르다
import sys
sys.stdin = open('09.txt', 'rt')
n = int(input())
coin = list(map(int, input().split()))
m = int(input())
dy = [1000]*(m+1)
dy[0] = 0
# 동전이 세개 있으므로 처음에 한개 있을때를 경우로
# 다 적용해보고 그다음 두개 째때를 적용해보고고for i in range(1, n+1):
for i in range(n):
    for j in range(coin[i], m + 1):
        # j만큼의 거스름 돈을 주려고 할 때
        # coin[i]를 반드시 쓴다고 가정할 때 동전 +1
        dy[j] = min(dy[j-coin[i]] + 1, dy[j])

print(dy[m])