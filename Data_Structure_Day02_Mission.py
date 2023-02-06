import random
import math

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

    x = math.sqrt(current.data[1]*current.data[1] + current.data[2]*current.data[2])
    print(f'{current.data[0]}건물, 거리 = {x}')
    while current.link != start:
        current = current.link
        x = math.sqrt(current.data[1] * current.data[1] + current.data[2] * current.data[2])
        print(f'{current.data[0]}건물, 거리 = {x}')
    print()


def make_point():
    """
    랜덤 좌표를 가지는 배열 만드는 함수
    :return: List
    """
    global data_array
    building_name = 'A'
    for i in range(10):
        data_array.append((building_name, random.randint(1,100),random.randint(1,100)))
        building_name = chr(ord(building_name)+1)

def make_liked_list(building):
    """
    거리가 작은 순서대로 circular Linked list 생성하는 함수
    :param building: 건물의 이름, 좌표(tuple)
    :return: void
    """
    global pre, current, head, memory
    node = Node(building)
    memory.append(node)

    if head == None:        # 첫번째 노드 생성
        head = node
        node.link = head
        return

    nx, ny = node.data[1:]
    ndistance = math.sqrt((nx*nx)+(ny*ny))  # 새노드까지의 거리
    hx, hy = head.data[1:]
    hdistance = math.sqrt((hx * hx) + (hy * hy)) # head가 가리키는 노드까지의 거리


    if hdistance > ndistance:
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        cx, cy = current.data[1:]
        cdistance = math.sqrt((cx * cx) + (cy * cy))  # current가 가리키는 노드까지의 거리
        if cdistance > ndistance:
            pre.link = node
            node.link = current
            return

    current.link = node
    node.link = head



memory = []
pre, current, head = None, None, None
data_array = []
if __name__ == "__main__" :
    make_point()  # data_array 생성
    for data in data_array:
        make_liked_list(data)
    print_nodes(head)
