# KEB Data Structure Day02
# Linked List_원형 연결 리스트 - insert, delete, find

class Node():
    def __init__(self, data):
        self.data = data
        self. link = None


def print_nodes(start):
    """
    node를 출력하는 함수 (단순 Linken List와 동일)
    :param start: 출력의 시작노드 data(String)
    :return: void
    """
    current = start
    if current.link == None :
        return

    print(current.data, end=" ")
    while current.link != start:
        current = current.link
        print(current.data, end=" ")
    print()


def insert_node(find_data, insert_data):
    global head, memory, pre, current  # 전역변수 사용
    if head.data == find_data:              # 첫번째 노드에 삽입할 경우
        node = Node(insert_data)                # 새로운 노드 생성
        node.link = head                        # 새로운 노드는 head를 가리킴
        last = head                             # 원형 List의 끝을 판별할 last 생성(head와 동일한 위치)
        while last.link != head :               # last가 head를 가리키기 전까지(리스트의 끝까지) 반복
            last = last.link                        # last를 이동
        last.link = node                        # (현재 last는 마지막 노드를 가리키고 있음) ==> last가 새로운 노드를 가리키게 함
        return
                                            # Linked List 중간에 삽입할 경우
    current = head                              # current 생성(head와 동일한 위치)
    while current.link != head:                 # current가 head를 가리키기 전까지(리스트의 끝까지) 반복
        pre = current                                   # pre 생성 (current와 동일)
        current = current.link                          # current가 다음 노드를 가리키도록 함
        if current.data == find_data:                   # 만약 current가 가리키는 노드가 원하는 위치의 노드라면
            node = Node(insert_data)                        # 새로운 노드 객체 생성
            node.link = current                             # 새로운 노드는 current(원하는 위치의 노드)를 가리킴
            pre.link = node                                 # pre가 가리키는 노드는 node를 가리킴
            return
                                            # Linked List 마지막에 삽입할 경우
    node = Node(insert_data)                    # 새로운 노드 객체 생성
    current.link = node                         # current는 새로운 노드를 가리킴
    node.link = head                            # 새로운 노드는 head가 가리키는 노드를 가리킴


def delete_node(delete_data):
    global memory, pre, current, head   # 전역변수 사용
    if head == delete_data:                 # 삭제하고자 하는 data가 head에 있을 경우
        current = head                              # current 생성 (head과 동일)
        head = head.link                            # head 한칸 이동
        last = head                                 # last 생성(head와 동일)
        while last.link != current:                 # last가 첫 노드(current)를 가리키지 않는 동안 반복
            last = last.link                            # last 한칸씩 이동
        last.link = head                            # last가 가리키는 노드(마지막 노드)가 head를 가리키게 함
        del (current)                               # current(delete할 노드) 삭제
        return
                                            # 삭제하고자 하는 data가 첫번째 이외의 노드에 있을 경우
    current = head                                  # current 생성 (head와 동일)
    while current.link != head:                     # current가 head(첫번째 노드)를 가리키지 않는 동안 반복
        pre = current                                   # pre 생성(current와 동일)
        current = current.link                          # current 한칸 이동
        if current.data == delete_data:                 # 만약 current data가 delete data와 같을 경우
            pre.link = current.link                         # pre노드를 current 다음 노드와 연결
            del(current)                                    # current 노드 삭제
            return


def find_node(find_data):
    """
    원형 Linked List에서 원하는 data를 가진 노드가 있는지 확인하는 함수
    :param find_data: 원하는 data(String)
    :return: (Node)
    """
    global memory, pre, head, current   #전역변수 사용
    current = head          # current 생성

    if current.data == find_data:           # 첫번째 노드가 찾는 노드일 경우
        return current                          # current 반환
    while current.link != head :            # current 가 가리키는 노드가 head(첫번쨰 노드)가 아닐경우 == 찾는 노드가 뒤에 있을 경우
        current = current.link                  # current 노드 한칸 이동
        if current.data == find_data:           # 만약 current가 카리키는 노드가 찾는 노드일 경우
            return current                          # current 반환
    return Node(None)                       # 찾는 노드가 Linkend List에 없는 경우 ==> 빈 노드 반환




memory = []
current, pre, head = None, None, None
data_array = ["히나타", "카게야마", "다이치", "니시노야"]


if __name__ == "__main__":
    # circular Linked List 생성
    ############################################################################
    node = Node(data_array[0])
    head = node
    node.link = node
    memory.append(node)

    for data in data_array[1:] :
        pre = node
        node = Node(data)
        pre.link = node
        node.link = head
        memory.append(node)

    print_nodes(head)
    #############################################################################

    # insert 확인 구문
    #############################################################################
    insert_node("카게야마", "나리타")  # 카게야마 앞에 나리타 삽입
    print_nodes(head)
    insert_node("다이치","야마구치")   # 다이치 앞에 야마구치 삽입
    print_nodes(head)
    #############################################################################

    #delete 확인 구문
    #############################################################################
    delete_node("야마구치")
    print_nodes(head)
    delete_node("나리타")
    print_nodes(head)
    #############################################################################

    #find 확인 구문
    #############################################################################
    print()
    print(find_node("히나타").data)
    print(find_node("츠키시마").data)
    #############################################################################