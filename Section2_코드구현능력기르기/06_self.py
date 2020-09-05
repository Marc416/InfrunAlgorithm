N = int(input())
num = list(map(int, input().split()))
sum_num = []


def digit_sum(x):
    temp = 0
    while x > 0:
        temp += x % 10
        x = x // 10
    return temp


max_index = -1
max_value = -1
for idx, value in enumerate(num):
    sum_num.append(digit_sum(value))
    if max_value < sum_num[idx]:
        max_value = sum_num[idx]
        max_index = idx
        print(max_value, sum_num[idx])
else:
    print(sum_num)
    print(num[max_index])
