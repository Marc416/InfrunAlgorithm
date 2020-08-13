import sys

# 문제중 바이너리서치로 찾아야 하는 문제들이 있는데 
# 그것들의 특징은 답의 범위가 있다는 것임. 개중요

sys.stdin = open('02.txt', 'rt')

k, n = map(int, input().split())
line = []
largest = 0
res = 0
for _ in range(k):
    tmp = int(input())
    line.append(tmp)
    # 가장 큰값을 largest에 넣는다
    # 가장큰값을 찾는 이유는최대 길이를 구해야하는데 최대 길이가 될 수 있는 것을
    # 찾기 위함임
    largest = max(tmp, largest)


def Count(length):
    cnt = 0
    for x in line:
        cnt += (x // length)
    return cnt


# 왜 lt가 1임?
# 인덱스를 찾는게 아니고
# 1~ 832? 까지의 숫자중 가장 클 수 있는걸 찾는거싱기 때문
lt = 1
rt = largest
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        res = mid
        # 더좋은 답을 찾기위해 mid 1업
        lt = mid + 1
    else:
        rt = mid - 1
