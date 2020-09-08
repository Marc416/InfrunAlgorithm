import sys

sys.stdin = open('01.txt', 'rt')
length = []
res = ''
w =input()
dy = [0] * (len(w) + 1)
for cut in range(1, len(w) // 2 + 11):
    # 잠깐 왜 여기 카운트는 1개지?
    cnt = 1
    # w를 j까지만큼 자르겠다는 것임
    # j가 1이면 0인덱스까지
    tmp = w[:cut]
    # cut부터 len(w)까지 cut만큼 증가
    for i in range(cut, len(w), cut):
        if tmp == w[i:i+cut]:
            cnt +=1
        else:
            if cnt == 1:
                cnt = ''
            res += str(cnt) + tmp
            tmp = w[i:i+cut]
            cnt = 1
            print(tmp)

    if cnt ==1:
        cnt = ''
    res += str(cnt)+ tmp
    length.append(len(res))
    res = ''
print(length)



    # res = max(res, cnt)
    # print(res)
