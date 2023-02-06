class Node():
    def __init__(self, data):
        self.data = data
        self.plink = None   # 정방향 링크
        self.nlink = None   # 역방향 링크


def print_nodes(start):
    current = start
    print("정방향 ==>", end=" ")           # 정방향 출력
    print(current.data, end=" ")          # 첫번째 노드 출력
    while current.plink != None:          # 정방향 링크가 None이 아닐 때 까지
        current = current.plink           # current 한칸 이동 후 출력
        print(current.data, end=" ")

    print("\n역방향 ==>", end=" ")         # 역방향 출력
    while current.nlink != None:          # 역방향 링크가 None이 아닐 때 까지
        print(current.data, end=" ")      # 노드 출력 후 current 한칸 이동
        current = current.nlink
    print(current.data, end=" ")          # 출력 후 한칸 이동하여 역방향 마지막 노드가 출력되지 않았으므로 따로 출력

    # 동일 기능(print_nodes(start))
    # ***********************************************
    # def print_nodes(start):
        # current = start
        # if current.plink == None:
        #     return
        # print("정방향 ==>", end=" ")
        # print(current.data, end=" ")
        # while current.plink != None:
        #     current = current.plink
        #     print(current.data, end=" ")
        # print("\n역방향 ==>", end=" ")
        # print(current.data, end=" ")
        # while current.nlink != None:
        #     current = current.nlink
        #     print(current.data, end=" ")
    # ***********************************************
pre, current, head = None, None, None
data_array = ["카게야마", "히나타", "츠키시마", "타나카", "다이치"]

if __name__ == "__main__" :
    node = Node(data_array[0])
    head = node
    for data in data_array[1:]:
        pre = node
        node = Node(data)
        pre.plink = node        # 기존 노드의 정방향 링크를 새 노드와 연결
        node.nlink = pre        # 새 노드의 역방향 링크를 기존 노드와 연결

    print_nodes(head)