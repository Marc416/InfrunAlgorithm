import sys

sys.stdin = open('03.txt', 'rt')
li = list(range(21))
print(li)

# 포문의 언더바는 숫자 입력을 받지 않고 포문을 도는 것임. i를 선언하고 입력 하는 것도 메모리 소모이기 때문에 쓰임
for _ in (range(10)):
    # 시작점과 끝점 설정
    n, m = map(int, input().split())
    # 5개 순서의 숫자를 모두 하나씩 바꿀 필요없음. 스와핑 을 하면 n/2으로 만들 수 있음.
    # 몇번 교체할건지 체크
    # +1을 한 이유는 홀수개의 숫자를 스와핑 할경우를 생각해서임
    cnt = (m - n + 1)//2
    for j in range(cnt):
        #j를 더하는 이유> 양쪽에서 센터로 좁혀지기위함
        li[n+j], li[m-j] = li[m-j], li[n+j]

li.pop(0)
for i in li:
    print(i , end=' ')

