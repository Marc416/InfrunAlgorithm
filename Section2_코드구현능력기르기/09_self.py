n = int(input())
dice_num = []
dice_sum = []

max_index = -1
max_price = -1


def diceSum(x):
    if x[0] == x[1] == x[2]:
        return 10000 + x[0] * 1000
    elif x[0] == x[1] or x[0] == x[2]:
        return 1000 + x[0] * 100
    elif x[1] == x[2]:
        return 1000 + x[1] * 100
    else:
        return max(x) * 100


for i in range(n):
    dice_num.append(list(map(int, input().split())))
    temp = diceSum(dice_num[i])
    if max_price < temp:
        max_price = temp
        max_index = i
print(max_price)
