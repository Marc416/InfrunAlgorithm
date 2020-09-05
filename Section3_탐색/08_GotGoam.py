import sys

sys.stdin = open('08.txt', 'rt')

# 소스받기
n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))

# 명령줄 받기
m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            # 팝한 것을 append하겠다는 의미임
            li[h - 1].append(li[h - 1].pop(0))
    else:
        for _ in range(k):
            # 젤 뒤엣거를 꺼내서 0번자리에 insert하겠다
            li[h - 1].insert(0, li[h - 1].pop())

s = 0
e = n - 1
res = 0
for i in range(n):
    for j in range(s, e + 1):
        res +=li[i][j]
    if i <n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1

print(res)