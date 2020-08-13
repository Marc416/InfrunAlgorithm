import sys

sys.stdin = open('05.txt', 'rt')

n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    # meeting 리스트는 튜플로 만들었다
    meeting.append((s, e))

# sorted : 인자와 그안의 요소까지 오름차순정렬해버림
# key lambda를 쓰고 x : 이자리에 오는 인자의 값을 기준으로 리스트를 정렬하겠다는것임. 요소제외
meeting.sort(key=lambda x: (x[1], x[0]))
# 끝나는시간
et = 0
cnt = 0

# 리스트의 요소를 뽑아서 포문을 돌릴 수도 있다.
for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1
print(cnt)
