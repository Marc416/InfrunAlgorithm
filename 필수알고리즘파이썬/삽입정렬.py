arr = [1, 3, 2, 5, 4]


def insert_Sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        while i > 0 and arr[i - 1] > current:
            arr[i] = arr[i - 1]
            # 내려가면서 탐색 , i를 기준으로 와일문에서 내려감
            i -= 1
        arr[i] = current


insert_Sort(arr)
print(arr)
