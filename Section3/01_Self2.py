n = int(input())

for i in range(n):
    word = input().upper()
    print(word)
    size = len(word)
    print(size)
    for j in range(size // 2):
        print(word[j], word[-1-j])
        if word[j] != word[-1 - j]:
            print('#%d NO' % (i + 1))
            break
    else:
        print('#%d YES' % (i + 1))
