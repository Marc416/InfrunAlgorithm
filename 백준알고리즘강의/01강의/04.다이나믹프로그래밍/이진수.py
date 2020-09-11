d = [[0] * 2 for _ in range(90 + 1)]
n = int(input())
d[1][1] = 1
d[2][0] = 1
for i in range(1, 90 + 1):
    if i > 1:
        d[i][0] = d[i - 1][0] + d[i - 1][1]
    if i > 2:
        d[i][1] = d[i - 2][0] + d[i - 2][1]

print(d[n])
