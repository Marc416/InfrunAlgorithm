import sys
sys.stdin = open('08.txt', 'rt')
n = int(input())
li = []
for _ in range(n):
    li.append(input())

while len(li) != 1:
    word = input()
    for i in range(len(li)):
        if li[i] == word:
            li.pop(i)
            break
print(li)
