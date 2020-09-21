boxes = [[1, 2], [2, 3], [3, 1]]
b = len(boxes)
ch = [0] * 1000
for i in boxes:
    for j in i:
        ch[j] += 1
for k in ch:
    if k >= 2:
        b -= 1
print(b)
