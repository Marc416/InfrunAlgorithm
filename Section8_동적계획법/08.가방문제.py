import sys
# 냅색알고리즘
sys.stdin = open('08.txt', 'rt')
n, m = map(int, input().split())
dy = [0] * (m+1)
for i in range(n):
    # weight, value
    w, v = map(int, input().split())
    # 현재 보고자하는 보석의 무게부터 j for문을 돌린다
    for j in range(w, m+1):
        dy[j] = max(dy[j], dy[j-w] + v)
print(dy[m])