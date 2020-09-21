import sys

sys.stdin = open('카카오1번.txt', 'rt')
new_id = input()
new_id = new_id.lower()
tmp = []
for i in new_id:
    if i.isdigit() or i.isalpha():
        tmp.append(i)
    elif i == '-' or i == '_':
        tmp.append(i)
    elif i == '.':
        # .이 두개 있으면 . 하나 더하지 않음
        if len(tmp) > 0 and tmp[-1] == i:
            continue
        else:
            tmp.append(i)
    else:
        continue
if len(tmp) > 0 and tmp[0] == '.':
    tmp.pop(0)
if len(tmp) > 0 and tmp[-1] == '.':
    tmp.pop(-1)
if len(tmp) == 0:
    tmp.append('a')
# 6단계 16개이상일 때 앞에 꺼만 자르기
if len(tmp) >= 16:
    tmp = tmp[0:15]
    if tmp[-1] == '.':
        tmp.pop(-1)
if len(tmp) <= 2:
    while len(tmp) != 3:
        tmp.append(tmp[-1])
new_id = ''.join(tmp)
print(new_id)
