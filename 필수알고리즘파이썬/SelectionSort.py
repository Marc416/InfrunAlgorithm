li = [12, 70, 25, 60, 60, 25]
# li = [20, 10, 7, 50, 70, 60]


#

# li = [17, 12, 25, 25, 25, 49, 60, 60, 75, 80]


def Selection_Sort(data):
    cnt = 0
    for i in range(len(data)):
        min = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min]:
                min = j
                cnt += 1

        temp = data[i]
        data[i] = data[min]
        data[min] = temp
        print(data)
    print(data, cnt)


def Partition(data, start, end):
    print('partion시작')
    pivot = end
    right = end - 1
    left = start
    while left < right:
        # 왼쪽 인덱스 옮기기(왼쪽 데이터가 피봇데이터 보다 작다면 우측으로 이동)
        while data[left] <= data[pivot] and left < right:
            left += 1
            print('피봇:', pivot, 'left인덱스:', left, 'right인덱스:', right)
        # 오른쪽거도 똑같이
        while data[right] >= data[pivot] and left < right:
            right -= 1
            print('피봇:', pivot, 'left인덱스:', left, 'right인덱스:', right)

        # left, right 데이터를 교환(left와 right사이에 뭐가 있다면 교환)#
        # if left < right and data[left] != data[right]:
        if left < right and data[left] != data[right]:
            print('Left,Right 교환 전', data, left, right)
            print('hey')
            data[left], data[right] = data[right], data[left]

            print('Left, Right 교환 후', data, left, right)
        else:
            print('Left, Right를  교환하지 않는다')

    print('피봇교환전', data, left, right)
    if data[pivot] < data[left]:
        data[pivot], data[left] = data[left], data[pivot]
    else:
        print('피봇을 교환하지 않는다')

    print('피봇교환후', data, left, right)
    return left


Lv = 1


def Quick_Sort(data, start, end, Lv):
    if start < end:
        next_end = Partition(data, start, end)
        print()
        print('Lv:', Lv, '좌측정렬', 'leftIdx:', start, 'rightIdx:', next_end - 1, 'pivot :', next_end)
        Quick_Sort(data, start, next_end, Lv + 1)
        print()
        print('Lv:', Lv, '우측정렬', 'leftIdx:', next_end + 1, 'rightIdx:', end - 1, 'pivot :', end)
        Quick_Sort(data, next_end + 1, end, Lv + 1)
        print()
        print('결과', data)
    else:
        print('leftIdx > rightIdx 더 커짐으로 아웃')


Quick_Sort(li, 0, len(li) - 1, Lv)
# newQuickSort(li, len(li) - 1, 0)
