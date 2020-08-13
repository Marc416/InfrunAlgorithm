import sys

sys.stdin = open('04.txt', 'rt')


# L은 a의 인덱스
def DFS(L, sum):
    # 시간복잡도를 줄이기위함. 원소합이 total보다 커지면
    # 아래의 원소들을 더할 필요없으므로 중간에 커트한다.
    if sum > total // 2:
        return

        # 트리의 마지막 구간에 도착시
    if L == n:
        if sum == (total - sum):
            print('Yes')
            # 프로그램종료
            sys.exit()
    else:
        # 왼쪽트리에 접근, L위치 원소 사용시
        DFS(L + 1, sum + a[L])  
        # L위치 원소 사용 안할 시
        DFS(L + 1, sum)


n = int(input())
a = list(map(int, input().split()))
total = sum(a)
DFS(0, 0)
