n = int(input())
score = list(map(int, input().split()))

ave = int(sum(score)/n + 0.5)
min =87788887
index = 0
indexScore =0
for idx, value in score:
    tmp = abs(ave-value)
    if min>tmp:
        min = tmp
        index = idx+1
        indexScore = value
    elif min == tmp:
        #옛날 스코어 indexScore가 현재 value스코어보다 크다면!!
        #이므로 다음인덱스에서 차이가 똑같으나 예전 스코어보다
        #크지않을 것이기 때문에 if문을 타지 않을것임
        if value > indexScore:
            indexScore = value
            index = idx +1