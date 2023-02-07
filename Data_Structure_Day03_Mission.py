# Day03_Mission03
# 도서관 대여도서 목록 출력하기 use binary search tree
import random


class Tree_node():
    def __init__(self):
        self.data = None
        self.llink = None
        self.rlink = None


def preorder(node) :
    """
    전위 순회 알고리즘
    :param node: 루트노드
    :return: void
    """
    if node == None:
        return
    print(node.data, end=' ')      # 1. 현재 노드 처리
    preorder(node.llink)            # 2. 왼쪽 서브트리 이동 (자기자신 호출) --> 재귀함수
    preorder(node.rlink)            # 3. 오른쪽 서브트리 이동 (자기자신 호출) --> 재귀함수


def make_tree():
    """
    이진트리 생성하는 함수
    :return: void
    """
    global root, rental_array
    node = Tree_node()
    node.data = rental_array[0]
    root = node

    for data in rental_array[1:]:

        node = Tree_node()
        node.data = data

        current = root
        while True:
            if data < current.data:
                if current.llink == None:
                    current.llink = node
                    break
                current = current.llink

            elif data == current.data:
                break

            else:
                if current.rlink == None:
                    current.rlink = node
                    break
                current = current.rlink
    print("\n이진 탐색 트리 구성 완료!\n")


root = None
data_array = ["어린왕자","생각의 탄생","총균쇠","자료구조","python","java","일반수학"]
rental_array = [random.choice(data_array) for i in range(15)]


if __name__ == "__main__":
    print(f'금일 대여 도서 목록 :{rental_array}')
    make_tree()
    print(f'금일 대여 도서 명 :',end=" ")
    preorder(root)





