import sys

sys.stdin = open('05.txt', 'rt')
n = int(input())
coin = []
money = [0] * 3
res = 2147000000
for _ in range(n):
    coin.append(int(input()))


def DFS(L):
    global res
    if L == n:
        # 가장 큰값에서 가장 작은 값을 찾아서빼준다
        cha = max(money) - min(money)
        # 중복된 수가 있는지 체크
        if cha < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            # set을 써서 세 수가 모두 다르다면 길이를 3 반환할것임
            # 맞으면 값 지정
            if len(tmp) == 3:
                res = cha
    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L + 1)
            money[i] -= coin[L]


DFS(0)
