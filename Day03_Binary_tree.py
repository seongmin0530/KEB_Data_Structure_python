# Day93_Binary Tree
# Like 폴더
# 이진트리 = 모든 노드의 자식이 최대 2개 : root --> 2--> 4 --> 8...
# 데이터 탐색에 용이...? ==> 로그 시간 보장(정렬되었을 때)
# 종류 1. 포화 이진 트리(full binary tree)      ==> 자식이 2개씩 꽉 차있는 트리(완전히 채워진 완전 이진트리)
# 종류 2. 완전 이진 트리(complete binary tree)  ==> 위에서부터 채워져있는 트리
# 종류 3. 일반 이진 트리                        ==> 위에서 부터 채워져있지 않고 채워져있는 트리
# 종류 4. 편향 이진 트리(skewed binary tree)    ==> 왼/오른쪽중 한쪽으로만 연결된 트리

# 차수 = 에지의 개수


# 이진트리 속 데이터 탐색
# 종류 1. 전위 순회(preorder traversal)       ==> 현재노드 처리 후 왼->오 순서의 서브트리로 이동
# 종류 2. 중위 순회(inorder traversal)        ==> 왼 서브트리 이동후 현재노드 처리 이후 오른쪽 서브트리로 이동
# 종류 2. 후위 순회(postorder traversal)      ==> 왼 -> 오 순서의 서브트리로 이동 이후 현재 노드 처리

class Tree_node():
    def __init__(self):
        self.data = None
        self. llink = None
        self. rlink = None


def preorder(node) :
    """
    전위 순회 알고리즘
    :param node: 루트노드
    :return: void
    """
    if node == None:
    # if not node: 같은 의미 ==> 트렌드....?
        return
    print(node.data, end='->')      # 1. 현재 노드 처리
    preorder(node.llink)            # 2. 왼쪽 서브트리 이동 (자기자신 호출) --> 재귀함수
    preorder(node.rlink)            # 3. 오른쪽 서브트리 이동 (자기자신 호출) --> 재귀함수


def inorder(node):
    """
    중위순회 알고리즘
    :param node: 루트노드
    :return: void
    """
    if node == None :
        return
    inorder(node.llink)             # 1. 왼쪽 서브트리 이동 (자기자신 호출) --> 재귀함수
    print(node.data, end='->')      # 2. 현재 노드 처리
    inorder(node.rlink)             # 3. 오른쪽 서브트리 이동 (자기자신 호출) --> 재귀함수


def postorder(node):
    """
    후위순회 알고리즘
    :param node: 루트
    :return: void
    """
    if node == None :
        return
    postorder(node.llink)           # 1. 왼쪽 서브트리 이동 (자기자신 호출) --> 재귀함수
    postorder(node.rlink)           # 2. 오른쪽 서브트리 이동 (자기자신 호출) --> 재귀함수
    print(node.data, end='->')      # 현재 노드 처리


root = None
data_array = [3, 2, 4, 1]

if __name__ == "__main__":


    # 데이터 삽입 in 이진탐색트리
    # ==> 현재 노드 기준 왼쪽 자식 노드 = (현재노드보다 작은 값), 오른쪽 자식 노드 = (현재노드보다 큰 값)
    ##################################################################################
    node = Tree_node()
    node.data = data_array[0]
    root = node

    for data in data_array[1:]:

        node = Tree_node()
        node.data = data

        current = root
        while True :
            if data < current.data :                # 입력하려는 데이터가 부모노드보다 작으면 왼쪽
                if current.llink == None :
                    current.llink = node
                    break
                current = current.llink

            else:
                if current.rlink == None :          # 입력하는 데이터가 부모노드보다 크면 오른쪽
                    current.rlink = node
                    break
                current = current.rlink
    print("make binary search tree complete!!")
    ##################################################################################


    # pre,in,postoder 확인
    ##################################################################################
    print("전위순회 확인 : ",end=" ")
    preorder(root)
    print("트리 끝")
    print("중위순회 확인 : ", end=" ")
    inorder(root)
    print("트리 끝")
    print("후위순회 확인 : ", end=" ")
    postorder(root)
    print("트리 끝")

    ##################################################################################


    # 데이터 검색 in 이진 탐색트리
    ##################################################################################
    find_data = int(input("탐색할 데이터값을 입력하세요. :"))

    current = root
    while True:
        if find_data == current.data :
            print(f'{find_data}(이)가 이진탐색 트리에 존재합니다!')
            break
        elif find_data < current.data :     # 찾으려는 데이터가 부모노드보다 작고
            if current.llink == None :          # 해당 부모노드가 왼쪽 link가 없다면
                print(f'{find_data}(이)가 이진탐색 트리에 존재하지 않습니다!')
                break
            current = current.llink         # 링크가 있다면 이동
        else:                               # 찾으려는 데이터가 부모노드보다 크고
            if current.rlink == None :          # 해당 부모도느가 오른쪽 링크가 없다면
                print(f'{find_data}(이)가 이진탐색 트리에 존재하지 않습니다!')
                break
            current = current.rlink         # 링크가 있다면 이동
    ##################################################################################


    # 데이터 삭제 in 이진 탐색 트리
    # (자식이 있는 노드와 리프노드로 나누어 생각해야 함)
    ##################################################################################
    # 리프노드 삭제            ==> 부모노드의 링크 None
    # 자식이 있는 노드 삭제     ==> 삭제할 노드의 부모노드를 삭제할 노드의 자식노드에 연결함(자식이 2개 있는 노드를 삭제할 때는 재귀 사용이 편함)
    delete_data = int(input("삭제할 데이터를 입력하세요. :"))
    current = root
    parent = None       # 용도 미정 변수. 176,177,183,184구문에서 current와 연결하여 node의 주소가 됨.
    while True :
        if delete_data == current.data :                # 1-1. 삭제할 데이터를 찾음

            if current.llink == None and current.rlink == None:         # 자식노드가 없을 때
                if parent.llink == current:             # 2-1. 만약 부모노드의 왼쪽 링크가 삭제하려는 노드와 연결되어있다면
                    parent.llink == None                # 3-1. 부모노드의 왼쪽 링크 삭제
                else :                                  # 2-2. 만약 부모노드의 오른쪽 링크가 삭제하려는 노드와 연결되어있다면
                    parent.right = None                 # 3-2. 부모노드의 오른쪽 링크 삭제
                del(current)                            # 4. 해당 노드 삭제

            elif current.llink != None and current.rlink == None :      #왼쪽 자식노드는 있으나 오른쪽 자식노드는 없을 때
                if parent.llink == current:             # 2-1. 부모노드의 왼쪽 링크가 삭제할 노드와 연결되어있다면
                    parent.llink = current.llink        # 3-1. 부모노드의 왼쪽 링크를 삭제할 노드의 왼쪽 자식노드와 연결
                else :                                  # 2-2. 부모노드의 오른쪽 링크가 삭제할 노드와 연결되어 있다면
                    parent.right = current.llink        # 3-2. 부모노드의 오른쪽 링크를 삭제할 노드의 왼쪽 자식노드와 연결
                del(current)                            # 4. 해당 노드 삭제

            elif current.llink == None and current.rlink != None :      # 왼쪽 자식노드는 없으나 오른쪽 자식노드는 있을 때
                if parent.llink == current:
                    parent.llink = current.rlink
                else :
                    parent.rlink = current.rlink
                del(current)

            print(f'{delete_data}가 삭제되었습니다.')
            break

        elif delete_data < current.data :               # 1-2. 삭제할 데이터가 현재 노드 데이터보다 작을 때
            if current.llink == None:                   # 2 현재 노드에서 왼쪽 링크가 없을 때(리프노드일 때)
                print(f'{delete_data}(이)가 트리에 없습니다.')
                break                                   # 3 트리에 삭제할 데이터 없음
            parent = current                            # 2. 부모노드 한칸 아래로 이동
            current = current.llink                     # 3. 현재 노드 한칸 아래로 이동

        else:                                           # 1-3. 삭제할 데이터가 현재 노드보다 클 때
            if current.rlink == None:                   # 2.현재 노드에서 오른쪽 링크가 없을 때(리프노드일 때)
                print(f'{delete_data}(이)가 트리에 없습니다.')
                break                                   # 3. 트리에 삭제할 데이터 없음
            parent = current                            # 2. 부모노드 한칸 아래로 이동
            current = current.rlink                     # 3. 현재 노드 한칸 아래로 이동
    preorder(root)
    ##################################################################################