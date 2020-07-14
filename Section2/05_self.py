n, m = map(int, input().split())
cnt =[0]*(n+m+1)
max =-1
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j]+=1
        if max < cnt[i+j]:
            max = cnt[i+j]

for i in range(len(cnt)):
    if cnt[i] ==max:
        print(i, end=' ')