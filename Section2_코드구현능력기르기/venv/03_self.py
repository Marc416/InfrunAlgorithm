n, k = map(int, input().split())
card = list(map(int, input().split()))

cardset = set()
for i in range(len(card)):
    for j in range(i+1, len(card)):
        for m in range(j+1, len(card)):
            cardset.add(card[i]+card[j]+card[m])


cardset = list(cardset)
cardset.sort(reverse=True)  #리버스 하는 순서가 중요함
print(cardset[k-1])
