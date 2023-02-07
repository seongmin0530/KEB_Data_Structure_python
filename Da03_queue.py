# Day03_ Queue
# 삽입 ==> rear 이동, 삭제 ==> front 이동
# queue가 비어있는 상태 ==> front == rear
# queue size 만큼 삽입, 삭제 후에 front, rear 위치 = SIZE-1 ==> 원형 queue로 해결...?
# 기본적인 큐 삽입 종료후 여러번 삭제하면 queue가 다 차지 않았으나 코드상 꽉 찼다고 인식하는 경우 발생 ==> is_queue_full 개선으로 해결
def is_queue_full():
    """
    queue의 상태를 확인하는 함수(가득 찼을 때 True 반환)
    :return: True/False
    """
    global SIZE, queue, front, rear
    if rear != SIZE -1 :                        # rear의 위치가 queue의 끝 인덱스가 아니라면 queue가 꽉 찬 것이 아님
        return False                                # False 반환
    elif rear == SIZE-1 and front == -1 :        # rear의 위치가 queue의 끝 인덱스이고 front가 -1이라면 queue가 꽉 찬 것임
        return True                                 # True 반환
    else :                                      # rear의 위치는 queue의 끝이지만 front가 -1이 아닐 때 (queue가 꽉 찬 척 할 때)
        for i in range(front+1, SIZE):          # queue에 있는 자료들 한칸씩 이동
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1                              # queue가 이동했으니 front와 rear도 1칸씩 줄임
        rear -= 1
        return False                            # queue가 안찼으니 False 반환


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
    rear += 1
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
    front += 1
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


SIZE = int(input("queue 크기를 입력해주세요. : "))
queue = [None for i in range(SIZE)]
front = -1      # 출구
rear = 0

if __name__ == "__main__" :
