n = int(input())
word = [list(input()) for i in range(n)]
reverseWord = []
generalWord = []

for i in word:
    tmp = i
    tmp = ''.join(tmp).upper()
    generalWord.append(tmp)
    reverseWord.append(''.join(i[::-1]).upper())

idx = 0
judge = 'Yes'
for i in generalWord:
    if i == reverseWord[idx]:
        judge = 'Yes'
    else:
        judge = 'No'

    print('#%d %s' % (idx + 1,judge))
    idx += 1

print(reverseWord)
print(generalWord)
