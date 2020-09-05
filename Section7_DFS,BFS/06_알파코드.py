import sys
#알파코드 It's very hard

sys.stdin = open('06.txt', 'rt')
code = list(map(int, input()))
n = len(code)
# 마지막수인것을 알려주기 위해 마지막에 -1을 넣기
# 2자리수체크할 때 code[L+1]에서 out of range를 없애기위함
code.insert(n, -1)
# n+3을 넣는 이유가 뭔지 잘 모르겟음
res = [0] * (n+3)
cnt = 0


def DFS(L, p):
    global cnt
    if L == n:
        cnt += 1
        for j in range(p):
            print(chr(res[j]+64), end = ' ')
        print()
        return
    else:   
        for i in range(1, 27):
            # 1~9까지의 수를 먼저 체크! 
            # 일의 자리수단위로 잘라서 체크하기
            if code[L] == i:
                res[p] = i
                DFS(L + 1, p + 1)
            # i//10 <- 두자리수중 앞자리 ex) '28'<-'2'
            # i%10 <- 두자리수중 뒷자리 ex) '28'<-'8'
            elif i >= 10 and code[L] == i // 10 and code[L + 1] == i % 10:
                res[p] = i
                DFS(L+2, p+1)

DFS(0, 0)
