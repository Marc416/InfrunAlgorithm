T = int(input())
N, s, e, k = map(int, input().split())

for i in range(T):
    arr = list(map(int, input().split()))
    arr = arr[s - 1:e]
    arr.sort()
    print('#%d %d' % (i + 1, arr[k - 1]))
