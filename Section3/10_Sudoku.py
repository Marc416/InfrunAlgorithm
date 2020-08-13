import sys

sys.stdin = open('10.txt', 'rt')

li = []
for _ in range(9):
    li.append(list(map(int, input().split())))


def check(temp):
    # 가로세로 탐색
    for i in range(9):
        # 1부터 9까지의 체크리스트만들기 가로 세로
        # 숫자가있는지 없는지 체크할 때는 견문색을 쓰는거다
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            # 가로탐색 후 1 대입 
            ch1[temp[i][j]] = 1
            # 세로탐색 후 1 대입 
            ch2[temp[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False

    # 그룹체크
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[temp[i * 3 + k][j * 3 + s]] = 1
            if sum(ch3) != 9:
                return False
        return True


if check(li):
    print('Yes')
else:
    print('No')
