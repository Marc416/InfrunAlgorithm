# li = [12, 70, 25, 60, 60, 25]
# li = [1, 2, 3, 2, 1]
li = [2, 1, 3, 2]


# li = [20, 10, 7, 50, 70, 60]
# li = [17, 12, 25, 25, 25, 49, 60, 60, 75, 80]


def QuickSort(data, left_index, right_index):
    if left_index < right_index:
        pivot_position = Partition(data, left_index, right_index)
        QuickSort(data, left_index, pivot_position - 1)
        QuickSort(data, pivot_position + 1, right_index)
        return
    else:
        print('left_index > right_index 이유로 아웃')


def Partition(data, left_pointer, right_pointer):
    pivot_idx = right_pointer

    right_pointer -= 1
    # left포인터가 right포인터를 넘어가거나 같아질 때까지
    while True:
        # 같다라는 조건이 있다는 것은 중복 값을 뛰어 넘겠다. 중복값을 좌측 정렬에 끼어 넣겠다는것 또는 우측 정렬에 끼워넣겠다는 것
        while data[left_pointer] < data[pivot_idx] and left_pointer < len(li) - 1:
            left_pointer += 1
        # 왜 이곳에만 크거나 같다라고 되어 있는 것인가(중복을 허용하기 위함)
        while data[right_pointer] >= data[pivot_idx] and right_pointer > 0:
            right_pointer -= 1
        # 포인터들 끼리 만나면 종료
        if left_pointer >= right_pointer:
            break
        else:
            data[left_pointer], data[right_pointer] = data[right_pointer], data[left_pointer]
            print('left, right 교환:', data)
    if data[left_pointer] != data[pivot_idx]:
        data[left_pointer], data[pivot_idx] = data[pivot_idx], data[left_pointer]
        print('left, pivot 교환:', data)
    else:
        print('left 와 pivot의 값이 같음으로 교환없음')
    # left 포인터와 right 포인터 어떤걸 반환해도 된다고 생각했는데 안된다. left만 반환해야 한다. 이유가 뭘까
    return left_pointer


QuickSort(li, 0, len(li) - 1)
print(li)
