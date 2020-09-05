import sys
sys.stdin = open('05.txt', 'rt')

def DFS(idx, sum, tsum):
    global result
    # 시간단축을 하기위한 커팅
    # total:전체 집합의 합
    # tsum:현 idx까지의 모든 원소합 
    # total에서 tsum을 빼면 나머지 원소를 합쳤을 때의 값이나옴
    if sum+(total-tsum) < result:
        return

    if sum > c:
        return
    if idx == n:
        if sum > result:
            result = sum
    else:
        DFS(idx + 1, sum + a[idx], tsum + a[idx])
        DFS(idx + 1, sum, tsum + a[idx])


if __name__ == '__main__':
    c, n = map(int, input().split())
    a = list(int(input()) for _ in range(n))
    # 상대적으로 크거나 작은 수를 도출해 내려면 전역변수를 만들어 비교할 수 있도록 해야함
    # 그래서 result에 값을 변경하면서 비교
    result = -2147000000
    total = sum(a)
    DFS(0, 0, 0)
    print(result)
