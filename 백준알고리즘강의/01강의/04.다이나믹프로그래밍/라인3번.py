n = 10007
n = str(n)

mini = 12575000

# answer = []
def DFS(l, num):
    global mini, answer
    if len(num) == 1:
        answer.append(l)
        answer.append(int(num))
        return
    else:
        cnt = num
        for i in range(1, len(num)):
            a = num[:i]
            b = num[i:]
            if a[0] == '0' or b[0] == '0':
                continue
            cnt = int(num[:i]) + int(num[i:])
            mini = min(mini, cnt)
        DFS(l + 1, str(mini))

# DFS(0, n)
# print(answer)

answer = []
def solution(n):
    DFS(0, n)
    return answer

print(solution(n))