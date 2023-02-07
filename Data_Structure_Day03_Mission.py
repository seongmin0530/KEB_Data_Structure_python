# Day03_Mission01
# 방방 대기시간 use circular queue
def is_queue_full():
    """
    queue의 상태를 확인하는 함수(가득 찼을 때 True 반환)
    :return: True/False
    """
    global SIZE, queue, front, rear
    if (rear+1)%SIZE == front   :                  # rear의 위치가 queue의 끝 인덱스가 아니라면 queue가 꽉 찬 것이 아님
        return True                               # False 반환
    else :
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
    if(is_queue_full()):
        print("queue가 꽉 찼습니다.")
        return True
    rear = (rear+1) % SIZE
    queue[rear] = data


def de_queue():
    """
    queue의 데이터를 삭제하는 함수
    :return: 삭제할 데이터
    """
    global SIZE, queue, front, rear
    if is_queue_empty() :
        # print("queue가 텅텅 비어있습니다.")
        return None
    front  = (front+1) % SIZE
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
    return queue[front + 1]


SIZE = 6
queue = [None for i in range(SIZE)]
front = 0     # 출구    (초기에 출구는 입구와 같은 위치여야 함)
rear = 0       # 입구    (-1이어야 처음부터 자료가 들어감)
total_wait = 0;

if __name__ == "__main__" :
    data_array = [("최고코스",60), ("중간코스",30), ("간편 코스",15), ("예약안내",10), ("간편코스",15)]

    print(f'예상 대기시간은 {total_wait}분 입니다.')
    print(f'방방 대기손님 내역 : {queue}\n')
    for data in data_array:
        total_wait += data[1]
        en_queue(data)
        print(f'예상 대기시간은 {total_wait}분 입니다.')
        print(f'방방 대기손님 내역 : {queue}\n')
    print("예상 대기시간 보기를 종료합니다.")
