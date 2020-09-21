a = ['a,b,c', 'v']
b = ['a,b']
for i in a:
    print(i)
    if b not in i:
        print('yes')
