import sys

sys.stdin = open('카드구매하기', 'rt')
n = int(input())
c = list(map(int, input().split()))
c.insert(0, 0)
dy = [0] * (n + 1)
for i in range(1, n + 1):
    # i개 뽑을 때
    for j in range(1, i + 1):
        # i-j인 이유가 뭘까 ????

        dy[i] = max(dy[i], dy[i-j]+c[j])
print(dy[n])
