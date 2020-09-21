info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]

# 효율성에서 떨어짐.. 어디서 떨어진지 알수 없음

infodb = []
for a in info:
    infodb.append(list(map(str, a.split())))

for i in query:
    tmp = i.split()

    iqry = []
    for j in tmp:
        if j == 'and':
            continue
        else:
            iqry.append(j)

    cnt = 0

    for k in infodb:
        if int(k[-1]) < int(iqry[-1]):
            continue
        for h in iqry[:-1]:
            if h == '-':
                continue
            if h not in k:

                break
        else:
            cnt += 1
    else:
        print(cnt)
