import sys

sys.stdin = open('02.txt', 'rt')

s = input()
# 길이를 나타내는 리스트
li = []
cnt = 0
for i in range(len(s)):
    # (이면 리스트에 추가하기
    if s[i] == '(':
        li.append(s[i])
    else:
        # )이면 이 전꺼가 (인지 확인
        if li[-1] == '(':
            li.pop()
            cnt +=len(li)
        # )이거 이면 리스트에 있는거 빼고
        else:
            li.pop()
            cnt+=1

print(cnt)