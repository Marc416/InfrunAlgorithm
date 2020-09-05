import sys

sys.stdin = open('03.txt', 'rt')

n, m = map(int, input().split())

li = list(map(int, input().split()))

lt = 1
rt = sum(li)


def Count(length):
    # cnt 1로 꼭 초기화 해야 하는가..?(내가 생각한건 0인데)
    cnt = 1
    sum = 0
    for i in li:
        # if sum +i => length:
        # 아 크거나 같으면 안되는 이유! 1,2,3 을 담는 용량 6분짜리라 가정하면
        # 이전에 쓰인 3을 다음 앨범 4,5,6... 에서 3을 다시 쓰이게되는구먼
        # 주의할것!
        if sum +i > length:
            cnt += 1
            sum = i
        else:
            sum += i
    return cnt


minLength = 0
res = 0
maxx = max(li)
while lt <= rt:
    mid = (lt + rt) // 2
    # 이부분 다시 공부
    if mid > maxx and Count(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)
