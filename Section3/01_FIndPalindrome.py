n = int(input())
word = [list(input()) for i in range(n)]

for i in word:
    tmp = ''.join(i).upper()
    for j in range(i,-1)
    reverseWord = ''.join(i.sort(reverse=True)).upper()
    print(tmp, i)
    if i == reverseWord:
        print('#% %' % (i + 1, 'YES'))
    else:
        print('#% %' %(i+1, 'NO'))

