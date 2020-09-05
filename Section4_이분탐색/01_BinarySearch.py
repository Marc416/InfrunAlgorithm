import sys

sys.stdin = open('01.txt', 'rt')

n, m = map(int, input().split())
a = list(map(int, input().split()))
# 오름차순 정렬
a.sort()
# 왼쪽 오른쪽 포인터
lt = 0
rt = n - 1
# lt가 rt보다 커지면 종료시킨다.
while lt <= rt:
    # 중간점을 찾아준다 변경이 계속되야하므로 안에 변수를 만들기
    mid = (lt + rt) // 2
    if a[mid] == m:
        # mid는 현재 인덱스임. 몇번째인지 고르기위해서는 01234 순이 아닌 1234순으로 변경
        # 그래서 mid에 1을 더한다
        print(mid + 1)
        break
    elif a[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1
else:
    print('값이 안에 없다')
