import sys

sys.stdin = open('07.txt', 'rt')
n = int(input())
tree = []
for _ in range(n):
    tree.append(list(map(int, input().split())))

res = 0
# s, e라는 플래그를 이용해서 s부터 e까지를 검색할수 있게하기
s = e = n // 2
for i in range(n):
    # e까지라는 것을 포함시키려면 e에 +1을 해준다
    for j in range(s, e + 1):
        res += tree[i][j]
    if i < n // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(res)
