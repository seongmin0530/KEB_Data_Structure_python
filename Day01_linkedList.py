# KEB Data Structure Day02
# Linked List_원형 연결 리스트 - count_odd_even

import random


class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


def print_nodes(start):
    current = start
    if current == None :
        return
    print(current.data, end=' ')
    while current.link != start:  #
        current = current.link
        print(current.data, end=' ')
    print()


def insert_nodes(find_data, insert_data):
    global head, current, pre
    if head.data == find_data:
        node = Node(insert_data)
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
        if current.data == find_data:
            node = Node(insert_data)
            node.link = current
            pre.link = node
            return
    node = Node(insert_data)
    current.link = node
    node.link = head


def delete_nodes(delete_data):
    global head, current, pre
    if head.data == delete_data:
        current = head
        head = head.link
        last = head  #
        while last.link != current:  #
            last = last.link  #
        last.link = head  #
        del current
        return
    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == delete_data:
            pre.link = current.link
            del current
            return


def find_nodes(find_data):
    global head, current, pre
    current = head
    if current.data == find_data:
        return current
    while current.link != head:  #
        current = current.link
        if current.data == find_data:
            return current
    return Node(None)


def is_find(find_data):
    """
    연결 리스트안에서 원소 존재 여부 판정 함수
    :param find_data: 찾고자 하는 원소. str
    :return: 연결 리스트안에서 원소가 존재하면 True리턴 아니면 False
    """
    global head, current, pre
    current = head
    if current.data == find_data:
        return True
    while current.link != head:  #
        current = current.link
        if current.data == find_data:
            return True

    return False


def count_odd_even():
    """
    입력된 데이터에서 홀수/짝수 개수 구하는 함수
    :return: 홀수/짝수 개수(int)
    """
    global head, current

    even, odd = 0, 0

    # SRP 위배
    # if head == None:
    #     return False

    current = head          # current 생성
    while True:             # 무한 반복
        if current.data % 2 == 0:   # current.data가 짝수라면
            even = even + 1         # even ++
        else:                       # current.data가 홀수라면
            odd = odd + 1           # odd ++
        if current.link == head:    # 만약 Linked list를 끝까지 다 탐색했다면
            break                   # while문 탈출
        current = current.link      # current 한칸 이동

    return odd, even                # even, odd 반환


def makeSquareNumber(odd, even):
    if odd > even:
        remainder = 1
    else:
        remainder = 0

    current = head          #current 생성
    while True:             #무한 반복
        if current.data % 2 == remainder:      # 홀수>짝수, current.data : 홀수 또는 홀수 < 짝수, current.data : 짝수일 때
            current.data = current.data * current.data  # current.data 제곱해서 저장
        if current.link == head:               # Linked list의 끝까지 탐색했다면
            break                              # 반복문 탈출
        current = current.link                 # current 한칸 이동


head, current, pre = None, None, None
data_array = list()

if __name__ == "__main__":
    # odd_even = count_odd_even()  # False 리턴
    for _ in range(7):
        data_array.append(random.randint(1, 10))

    node = Node(data_array[0])
    head = node
    node.link = head
    for data in data_array[1:]:
        pre = node
        node = Node(data)
        pre.link = node
        node.link = head

    print_nodes(head)
    odd_even = count_odd_even()
    print(f'Odd Number : {odd_even[0]}, Even Number {odd_even[1]}')
    makeSquareNumber(odd_even[0], odd_even[1])
    print_nodes(head)