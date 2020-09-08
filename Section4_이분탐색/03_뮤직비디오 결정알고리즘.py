import sys

sys.stdin = open('03.txt', 'rt')

n, m = map(int, input().split())

li = list(map(int, input().split()))

lt = 1
rt = sum(li)

# DVD의 개수
def Count(capacity):
    # cnt 1로 꼭 초기화 해야 하는가..?(내가 생각한건 0인데)
    # 답 : DVD 1개는 무조건 생성되는 것이기 때문에 1이 맞음
    cnt = 1
    # 길이
    sum = 0
    for i in li:
        # if sum +i => length:
        # 아 크거나 같으면 안되는 이유! 1,2,3 을 담는 용량 6분짜리라 가정하면
        # 이전에 쓰인 3을 다음 앨범 4,5,6... 에서 3을 다시 쓰이게되는구먼
        # 주의할것!
        
        # 곡을 추가할 때 용량을 초과하는지 체크 
        if sum +i > capacity:
            # i곡의 용량이 초과하기 때문에 DVD한장을 추가한다
            cnt += 1
            # 새로운 sum이라는 DVD에 초과한 i의 곡을 담는다
            sum = i
        else:
            sum += i
            print('sum',sum)
    return cnt


minLength = 0
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    # 이부분 다시 공부
    # 나눌트랙의 길이가 Max보다 크고 : 이게 뭔소리지?
    # mid만큼 길이의 음악을 DVD에 넣을 경우 만들어 지는 DVD의 수
    if Count(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)
