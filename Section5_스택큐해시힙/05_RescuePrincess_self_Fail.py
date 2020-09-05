import sys

sys.stdin = open('05.txt', 'rt')

n, k = map(int, input().split())

li =[]
for i in range(n):
    li.append(i)

while len(li) !=k:
    li.pop(k-1)
print(li[k-1])