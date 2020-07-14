n = int(input())
num = [0]*(n+1)

num[0]=1
num[1]=1

for i in range(2, n+1):
    if num[i] != 0:
        for j in range(2, i):
            if i%j ==0:
                num[i:i]=1

a = [1,2,3,4,5,]
a[2::2] = 0
print(a)