import sys

sys.stdin = open('09.txt', 'rt')
a = input()
b = input()
str1 = [0]*52
str2 = [0]*52

for x in a:
    if x.isupper():
        # ord => 아스키코드로변환
        # 대문자A는 65 로 65를빼서 0번 리스트에 카운트를 해준다
        str1[ord(x) - 65] += 1
    else:
        # 소문자 a 는 97이 나옴 대문자가 0번부터 25번까지 26가지 인덱스를 쓰고있으므로
        # 97-71 = 26 번 인덱스를 쓸 수 있게 71을 빼주기
        str1[ord(x) - 71]

for x in b:
    if x.isupper():
        str2[ord(x) - 65] += 1
    else:
        str2[ord(x) - 71]

for i in range(52):
    if str1[i] != str2[i]:
        print('no')
        break
else:
    print('yes')

