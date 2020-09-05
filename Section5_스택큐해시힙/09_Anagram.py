import sys

sys.stdin = open('09.txt', 'rt')
a = input()
b = input()
str1 = dict()
str2 = dict()

for x in a:
    # get:x라는 값이 있냐? 없으면 0을 줘라
    # get을 쓰는 이유: str[x] += 1 <-이게 안되기 때문
    str1[x] = str1.get(x, 0) + 1
for x in b:
    str2[x] = str2.get(x, 0) + 1

# str1의 키값들만 접근하고 싶은 경우
for i in str1.keys():
    if i in str2.keys():
        # str1[i] 는 밸류를 접근 하는 것임.
        # str1[a]와 같은 의미임 이게 i로 되어 있어서 헷갈렸네
        if str1[i] != str2[i]:
            print("no")
            break
    # 비교하는 문자열에 없는 알파벳이 있을 경우
    else:
        print('no')
        break
else:
    print('yes')
