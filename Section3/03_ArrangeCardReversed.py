card = []
for i in range(1, 21):
    card.append(i)

for i in range(10):
    n, m = map(int, input())
    n = n * (i + 1)
    m = m * (i + 1)
    if n >= 20:
        n = 20
    elif m >= 20:
        m = 20

    for j in range(n-1, m):
        print(j, end= ' ')
