# 메모리제이션!!!! 매우 중요 메모리제이션을 안하면
# 그냥 재귀에 불과함
import sys
sys.stdin = open('1.txt', 'rt')
n = int(input())
# n+1하는 이유는 1번인덱스부터 쓰기 위함
dy = [0] * (n + 1)


def DFS(len):
    # 메모리제이션
    # 이미 구한 결과값이면 끌어와서 쓰겠다는 것임
    if dy[len] > 0:
        return dy[len]
    if len == 1 or len == 2:
        return len
    else:
        dy[len] = DFS(len - 1) + DFS(len - 2)
        return dy[len]


print(DFS(n))
