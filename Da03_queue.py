# Day03_ Queue - 원형 queue
# is_queue_full => elif에서 자료를 옮기는 부분이 자료의 size가 커지면 굉장히 과정이 길어짐 -> 엄청난 오버헤드
# 원형 queue로 해결
# 선형 queue와 다르게 0부터 시작
# 선형 queue와 다르게 % SIZE를 해줘 원형으로 이어줌
# 단점 --> 한칸의 공간 을 못쓰게 됨 (SIZE-1개의 공간만 사용할 수 있기 때문에) ==> 꽉차게 쓰면 컴퓨터는 queue가 빈 것을 이해함(front == rear이기 때문)
def is_queue_full():
    """
    queue의 상태를 확인하는 함수(가득 찼을 때 True 반환)
    :return: True/False
    """
    global SIZE, queue, front, rear
    if(rear +1)%SIZE == front :         # 변화 : FRONT와 REAR가 같은 경우
        return True
    else:
        return False


def is_queue_empty():
    """
    queue의 상태를 확인하는 함수(비어있을 때 True 반환)
    :return: True/False
    """
    global SIZE, queue, front, rear
    if front == rear :          # front의 위치가 rear와 같다면 queqe가 비어있는 것임
        return True
    else :
        return False


def en_queue(data):
    """
    queue에 data 삽입하는 함수
    :param data: 삽입할 데이터
    :return: True(bool)
    """
    global SIZE, queue, front, rear
    if is_queue_full() :
        print("queue가 꽉 찼습니다.")
        return
    rear  = (rear+1) % SIZE                 # 변화 : 원형 형태로 이어주기 위해 %SIZE (기존 : raer += 1)
    queue[rear] = data


def de_queue():
    """
    queue의 데이터를 삭제하는 함수
    :return: 삭제할 데이터
    """
    global SIZE, queue, front, rear
    if is_queue_empty() :
        print("queue가 텅텅 비어있습니다.")
        return None
    front = (front+1) % SIZE                # 변화 : 원형 형태로 이어주기 위해 %SIZE(기존 : FRONT +=1)
    data = queue[front]
    queue[front] = None
    return data


def peek() :
    """
    queue의 다음에 반환할 data를 찾는 함수
    :return: 다음에 반환(삭제)할 값
    """
    global SIZE, queue, front, rear
    if is_queue_empty():
        return None
    return queue[(front + 1) % SIZE]        # 변화 : 원형 형태로 이어진 자료를 탐색하기 위해 %SIZE(기존 : front + 1)


SIZE = 10
queue = [None for i in range(SIZE)]
front = 0     # 원형 QUEUE이기 때문에 0부터 시작
rear = 0

if __name__ == "__main__" :
    data_array = ["a", "b", "c", "d"]
    for data in data_array:
        en_queue(data)
        print(data, end=" ")
    print()
    print(queue)

    for j in range(5) :
        print(de_queue(), end=" ")