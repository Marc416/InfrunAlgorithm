tree = 'xwbbw'

# 하나하나씩 떼어서 조건에 맞는지 검색하기에 좋은거 같음
def quad(loctree, ind):
    let = loctree[ind]
    # x가 있으면 뿌리를 내려 탐색하기 위한 기저조건
    if let == 'w' or let == 'b':
        return let
    ind += 1
    a = quad(loctree, ind)
    ind += len(a)
    b = quad(loctree, ind)
    ind += len(b)
    c = quad(loctree, ind)
    ind += len(c)
    d = quad(loctree, ind)
    ind += len(d)
    return 'x' + c + d + a + b


print(quad(tree, 0))
