word = input()
res = 0
for x in word:
    #if x.isdecimal() <- 0~9까지 숫자만 찾아주는 기능
    #if x.isdigit() <-2에 2승 3승 모든 숫자 다찾아줌
    if x.isdecimal():
       res = res*10+int(x)
print(res)

cnt = 0
add=[]
for i in range(1, res+1):
    if res % i ==0:
        add.append(i)
        cnt +=1

print(cnt)
print(add)