data = [80,75,25,60,60,17,49,12,25]


def Partition(data, start, end):
    pivot = end
    right = end - 1
    left = start
    while left < right:
        # 왼쪽 인덱스 옮기기(왼쪽 데이터가 피봇데이터 보다 작다면 우측으로 이동)
        while data[left] < data[pivot] and left < right:
            left += 1
        # 오른쪽거도 똑같이
        while data[right] >= data[pivot] and left < right:
            right -= 1

        # left, right 데이터를 교환(left와 right사이에 뭐가 있다면 교환)#
        if left < right and data[left] != data[right]:
            print('데이터교환전', data, left, right)

            data[left], data[right] = data[right], data[left]
            left += 1
            right -= 1
            print('교환후', data, left, right)

    print('피봇교환전2', data, left, right)
    if left >= right and data[pivot]<data[left]:
        data[pivot], data[left] = data[left], data[pivot]

    print('피봇교환후2', data, left, right)
    return left


def Quick_Sort(data, start, end):
    if start < end:
        next_end = Partition(data, start, end)
        print()
        print('end :', next_end, 'start:', start, '좌측정렬')
        Quick_Sort(data, start, next_end - 1)
        print()
        print('end:', next_end, 'start:', start, '우측정렬')
        Quick_Sort(data, next_end + 1, end)
        print()
        print('결과', data)
Quick_Sort(data, 0, len(data) - 1)