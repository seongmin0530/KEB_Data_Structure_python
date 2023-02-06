# KEB Data Structure Day01
# Linked List_insert_delete_find


class Node() :
    def __init__ (self, data) :  # None 생성자를 호출할 때 data를 입력받음
        self.data = data
        self.link = None


def print_nodes(start) :
    """
    Linked list로 구현된 데이터를 출력하는 함수
    :param start: 출력할 노드의 시작위치
    :return: void
    """
    current = start
    if current == None :
        return
    print(current.data, end = ' ')
    while current.link != None:
        current = current.link
        print(current.data, end = ' ')
    print()



def insert_nodes(find_data, insert_data):
    """
    Linked list에 data를 삽입하는 함수
    :param find_data: 찾고자 하는 데이터 (String)
    :param insert_data: 삽입할 데이터 (String)
    :return: void
    """
    global memory, head, current,pre                        # 전역변수로 선언된 변수들을 사용할 것.
    if head.data == find_data:      # 첫 번째 노드 삽입
        node = Node(insert_data)                            # 삽입할 데이터의 노드 생성
        node.link = head                                    # 삽입할 노드가 기존의 헤드(첫번째 노드)를 가리키게 함
        head = node                                         # 새로 삽입한 노드를 헤드로 만듬
        return

    current = head                                          # current를 기존의 head위치와 동일하게 설정
    while current.link != None:      # 중간 노드 삽입
        pre = current                                       # pre가 current를 가리키게 함
        current = current.link                              # current를 다음 노드로 이동(pre -> current 순서가 되도록)
        if current.data == find_data:                       # current노드가 삽입할 노드라면
            node = Node(insert_data)                            # 삽입할 데이터가 있는 노드 생성
            node.link = current                                 # 삽입할 데이터가 있는 노드가 가리키는 노드를 current(기존에 찾을 데이터)로 설정
            pre.link = node                                     # pre노드가 가리키는 것(삽입할 노드)를 현재노드로 설정
            return

    node = Node(insert_data)        # 마지막 노드 삽입
    current.link = node                                     # current노드(마지막 노드)의 다음 노드를 삽입할 데이터가 있는 노드로 설정



def delete_nodes(delete_data):
    """
    노드를 삭제하는 함수
    :param delete_data: 삭제할 데이터(String)
    :return: void
    """
    global head, current, pre

    if head.data == delete_data:            # 첫번째 노드가 삭제할 데이터일 때
        print('첫 번째 노드 삭제 완료')
        current = head                          # current노드를 head 노드로 설정
        head = head.link                        # head 노드가 가리키는 노드(두번째 노드)를 head노드로 설정
        del current                             # current노드(기존의 head 노드)를 삭제
        return

    current = head                          # 첫번째 노드 이외의 위치에 삭제할 데이터가 있을 때
    while current.link != None:                 # current 노드의 데이터가 Node일 때까지 반복
        pre = current                           # pre노드를 current노드로 설정
        current = current.link                  # current노드를 current 다음 노드로 설정
        if current.data == delete_data:         # 만약 current 노드의 데이터가 삭제할 데이터와 동일하다면
            print('중간 노드 삭제 완료')
            pre.link = current.link             # pre노드가 current노드의 다음데이터를 가리키도록 설정
            del current                         # current노드 삭제
            return

    print('삭제할 노드를 찾지 못함')


def find_nodes(find_data):
    """
    Linked List에 있는 임의의 데이터를 찾는 함수
    :param find_data: 찾을 데이터(String)
    :return: Node
    """
    global head, current, pre

    current = head                              # current노드 생성(Head노드와 동일한 위치에)
    if current.data == find_data:       # 첫번째 노드(current,head)가 찾고자 하는 노드일 때
        return current                          # 첫번째 노드 반환

    while current.link != None:         # 첫번째 이외의 위치에 찾고자 하는 노드가 있을 때(반복)
        current = current.link          # current노드를 다음 노드로 이동
        if current.data == find_data:   # current노드가 찾고자하는 노드일 때
            return current                  # 해당 current 노드 반환

    return Node(None)                   # 해당 데이터가 Linked list에 없을 때 --> 빈 노드 반환


memory = []
head, current, pre = None, None, None
data_array = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]


if __name__ == "__main__":
    node = Node(head)		#head node 생성
    node.data = data_array[0]
    head = node
    memory.append(node)

    for data in data_array[1:] :	#이후 노드 생성
        pre = node
        node = Node(data)
        node.data = data
        pre.link = node
        memory.append(node)


    # insert 기능 수행 확인
    print_nodes(head)  #현재 노드로 생성되어 있는 데이터를 순차적으로 출력
    insert_nodes("피카츄", "잠만보")  # 찾는 데이터인 피카츄 앞에 잠만보 삽입
    print_nodes(head)
    insert_nodes("푸린","어니부기")  # 찾는 데이터인 푸린 앞에 어니부기 삽입
    print_nodes(head)
    insert_nodes("성윤모","어니부기")  #찾는 데이터가 없으니 마지막 위치에 추가
    print_nodes(head)

    # delete 기능 수행 확인
    delete_nodes("잠만보")  # 첫번째 노드인 잠만보 삭제
    print_nodes(head)
    delete_nodes("어니부기") # 이후 중간에 위치한 어니부기 삭제
    print_nodes(head)
    delete_nodes("강찬석")  # 강찬석은 linked list에 없으므로 삭제 불가
    print_nodes(head)

    #find 기능 수행 확인
    print(find_nodes("파이리").data)  # Linked list에 파이리가 있으므로 파이리 출력
    print(find_nodes("박민석").data)  # Linked list에 박민석이 없으므로 None 출력