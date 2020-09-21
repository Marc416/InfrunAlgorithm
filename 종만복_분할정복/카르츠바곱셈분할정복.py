# https://nearkim.coffee/posts/karatsuba-python-implementation
def karatsuba(x, y):
    # 각각의 length를 구한다
    strx, stry = str(x), str(y)
    lenx, leny = len(strx), len(stry)

    # Initialize
    if lenx == 1 or leny == 1:
        return x * y

    # Divide
    # 두 수중 길이가 짧은것을 2개로 나눠 자를 인덱스 찾기
    m = min(lenx, leny) // 2
    a, b = int(strx[:-m]), int(strx[-m:])
    c, d = int(stry[:-m]), int(stry[-m:])

    # Conquer
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    # Combine
    return 10 ** (2 * m) * ac + 10 ** m * ad_bc + bd


print(karatsuba(60, 4))
