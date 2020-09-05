# 재귀를 이용해서 깊이 우선 탐색을 하자
import sys

sys.stdin = open('02.txt', 'rt')


# 전위순회 : 주로 많이 쓰임 
def DFS_MeFirst(v):
    if v > 7:
        print()
        return
    else:
        # 자기꺼 먼저하고 왼쪽 오른쪽 가면 전위순회
        print(v, end=' ')
        # 왼쪽 자식
        DFS_MeFirst(v * 2)
        # 오른쪽 자식
        DFS_MeFirst(v * 2 + 1)


# 중위순회 : 거의 안쓰인다고함 그건 모르는일
def DFS_LmomR(v):
    if v > 7:
        print()
        return
    else:
        # 왼쪽 자식
        DFS_LmomR(v * 2)
        # 자기꺼, 부모
        print(v, end=' ')
        # 오른쪽 자식
        DFS_LmomR(v * 2 + 1)

# 후위순회 : 병합정렬일 때 이거많이 씀
def DFS_LRmom(v):
    if v > 7:
        print()
        return
    else:
        # 왼쪽 자식
        DFS_LRmom(v * 2)
        # 오른쪽 자식
        DFS_LRmom(v * 2 + 1)
        # 부모꺼, 자기꺼
        print(v, end=' ')


DFS_MeFirst(1)
DFS_LmomR(1)
DFS_LRmom(1)




