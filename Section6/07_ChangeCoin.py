import sys

sys.stdin = open('07.txt', 'rt')
n = int(input())
c = list(map(int, input().split()))
m = int(input())
c.sort(reverse=True)


def DFS(L, sum):
    global res
    # 커팅: res가 최대로 설정되어 있다가 최소 depth로 바뀌고
    # L이 탐색하면서 res보다 더 내려가봐야 최소 res를 구하는데 불필요한 탐색이므로 return시킨다
    # 타임 리미트가 없는 알고리즘테스트면 이런게 필요없겠지만 알아두면 좋음
    if L > res:
        return

    if sum > m:
        return

    if sum == m:
        if res > L:
            res = L
    else:
        for i in c:
            DFS(L + 1, sum + i)


res = 2156870
DFS(0, 0)
print(res)
