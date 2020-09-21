orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2, 3, 5]
# for c in len(course):
#     # 비교할 단어 뭉치
for i in range(len(orders)):
    ch = [0] * len(orders[i])
    # 전체탐색
    for j in range(len(orders[i])):
        for k in orders:
            if orders[i][j] in k:
                ch[j] += 1
    print(ch)
    print()
