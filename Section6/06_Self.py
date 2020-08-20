import sys
sys.stdin=open('06.txt', 'rt')

n, m = map(int, input().split())
li = []
# for i in range(1, n+1):
#     li.append(i)

def DFS(L):
    if L==m:
        print(li)
        return
    else:
        for i in range(1, n+1):
            li.append(i)
            DFS(L+1)
            li.pop()

DFS(0)