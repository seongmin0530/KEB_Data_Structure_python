# KEB Data Structure Day01
# Linked List


class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None


def print_nodes(start) :
    current = start
    if current == None :
        return
    print(current.data, end = ' ')
    while current.link != None:
        current = current.link
        print(current.data, end = ' ')
    print()


memory = []
head, current, pre = None, None, None
data_array = ["피카츄", "꼬부기", "이상해씨", "롱스톤", "푸린"]


if __name__ == "__main__":
    node = Node()		#head node 생성
    node.data = data_array[0]
    head = node
    memory.append(node)

    for data in data_array[1:] :	#이후 노드 생성
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    print_nodes(head)
    print(node.data)
    print(pre.data)