import sys

sys.stdin = open('09.txt', 'rt')
a = input()
b = input()
sH = dict()

for x in a:
    sH[x] = sH.get(x, 0) + 1

# 겹치는 원소들 마이너스 카운트
for x in b:
    sH[x] = sH.get(x, 0) - 1

# 체크구간
for x in a:
    # 카운트 남는거 있으면
    if sH.get(x) >0:
        print('no')
        break
else:
    print('yes')
