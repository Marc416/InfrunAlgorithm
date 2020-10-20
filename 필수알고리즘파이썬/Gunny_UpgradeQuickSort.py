li = [12, 70, 25, 60, 60, 25]
# li = [1, 2, 3, 2, 1]
# li = [2, 1, 3, 2]


# li = [20, 10, 7, 50, 70, 60]
# li = [17, 12, 25, 25, 25, 49, 60, 60, 75, 80]


def QuickSort(data, left_index, right_index):
    if left_index < right_index:
        pivot_position = Partition(data, left_index, right_index)
        QuickSort(data, left_index, pivot_position - 1)
        QuickSort(data, pivot_position + 1, right_index)
    else:
        print('left_index > right_index 이유로 아웃')
        return


def Partition(data, left_pointer, right_pointer):
    pivot_idx = right_pointer
    i = left_pointer - 1
    # left포인터가 right포인터를 넘어가거나 같아질 때까지
    while left_pointer <= right_pointer-1:
        if data[left_pointer] <= data[pivot_idx]:
            i += 1
            data[i], data[left_pointer] = data[left_pointer], data[i]
        left_pointer += 1
    data[i + 1], data[right_pointer] = data[right_pointer], data[i + 1]
    return i + 1


QuickSort(li, 0, len(li) - 1)
print(li)
