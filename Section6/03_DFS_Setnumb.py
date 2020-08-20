import sys

sys.stdin = open('03.txt', 'rt')
n = int(input())
# 부분집합이기 때문에 ch를 쓴다?
ch = [0] * (n + 1)


def DFS(v):
    # 브레이크 지점
    if v == n + 1:
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end='')
        print()
    else:
        # 왼쪽으로 탐색
        ch[v] = 1
        DFS(v + 1)
        # 오른쪽으로 탐색
        ch[v] = 0
        DFS(v + 1)

# 1부터 시작하는 이유 : 연속된 자연수 체크하기에는
# 배열인덱스로 체크하기 좋으니까?
DFS(1)
