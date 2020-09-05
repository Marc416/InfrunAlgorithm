import sys

sys.stdin = open('04.txt', 'rt')

n = int(input())
ns = list(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))
# 플래그초기화
mflag = nflag = 0
# 결과물
res = []

while nflag < n and mflag < m:
    if ns[nflag] <= ms[mflag]:
        res.append(ns[nflag])
        nflag += 1
    else:
        res.append((ms[mflag]))
        mflag += 1

# while문 나가서
# 마지막에 남은 원소들은 어느 원소인지 체크
if nflag < n:
    # res 리스트에 남은 원소가있는 리스트를 슬라이스로 flag가 있는
    # 구간부터 끝까지 넣어준다.
    res = res + ns[nflag:]
else:
    res = res + ms[mflag:]

#프린트해주기
for i in res:
    print(i, end=' ')

