# 어떻게 보면 이게 리스트를 구현하는 것과 같다고 볼 수 있을거 같음
class Node:
    # 파이썬에서 init함수란 무엇인가?
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def initList():
    # 노드A가 글로벌로 선언되었는데 어디에도 노드A는 존재하지 않는다.
    # 어디에 선언된걸 쓴다는 것인가?
    global node_A
    node_A = Node('A')
    node_B = Node('B')
    node_D = Node('D')
    node_E = Node('E')
    node_A.next = node_B
    node_B.next = node_D
    node_D.next = node_E


def print_list():
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next
    print()


def delete_node(del_data):
    global node_A
    pre_node = node_A
    next_node = pre_node.next
    # 가장 첫번째 노드를 삭제할 때 조금 다름
    if pre_node.data == del_data:
        node_A = next_node
        # del 은 리스트를 삭제한다는 것임
        del pre_node
        return

    while next_node:
        if next_node.data == del_data:
            pre_node.next = next_node.next
            del next_node
            break
        pre_node = next_node
        next_node = next_node.next


def insert_node(data):
    global node_A
    new_node = Node(data)
    # 노드p와 노드 t는 새 노드가 안착할 위치를 알려
    # 과거의노드
    node_P = node_A
    # P:현재의노드 Present
    node_T = node_A
    while node_T.data <= data:
        node_P = node_T
        node_T = node_T.next

    # 새노드 위치가 결정되는 곳
    # node_T는 반복문 돌면서 data보다 커진 값임
    new_node.next = node_T
    # 값복사가 아니고 레퍼런스인건가
    # 응 그런듯 이닛함수 쓴게아니니까
    node_P.next = new_node

initList()
print_list()
print('노드C추가')
insert_node("C")
print_list()
print('노드D삭제')
delete_node('E')
print_list()
