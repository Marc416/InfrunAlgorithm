li = [2, 5, 23, 1, 3, 4]


def merge(left, right):
    v = list()
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            v.append(left[i])
            i += 1
        else:
            v.append(right[j])
            j += 1

    if i == len(left):
        v = v + right[j:len(right)]
        print('왼쪽나머지', v)
    if j == len(right):
        v = v + left[i:len(left)]
        print('오른쪽나머지', v)
    return v


def merge_sort(data):
    if len(data) <= 1:
        return data
    m = len(data) // 2
    left = merge_sort(data[0:m])
    right = merge_sort(data[m:len(data)])
    return merge(left, right)


# MergeSort(li, 0, len(li) - 1)
li =merge_sort(li)
print(li)
