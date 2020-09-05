import sys
sys.stdin = open('03.txt', 'rt')
n = int(input())
G = list(map(int, input().split()))
s = sum(G)
# 측정될 수 있는 그램을 중복없이 넣기 위함
res = set()
def DFS(L,sum):
    global res
    if L == n:
        if 0 < sum <=s:
            # 대칭 구도가 되는 형태이므로 음수는 체크하지 않아도됨.
            res.add(sum)
        return
    else:
        # L추를 왼쪽에다 넣겠다
        DFS(L+1, sum+G[L])
        # L추를 오른쪽에다 넣겠다
        DFS(L+1, sum-G[L])
        # L추를 넣지 않겠다
        DFS(L+1, sum)


DFS(0,0)
print(s-len(res))