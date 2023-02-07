# stack과 webbrowser,time 패키지을 이용하면 web사이트 방문 기록등을 확인할 수 있다.
# time을 사용하지 않으면 컴퓨터 사양에 따라 순방문 순서가 바뀔 수 도 있다.

import webbrowser
import time


SIZE = 100
stack = [None for i in range(SIZE)]
top = -1


def is_stack_full():
    global stack, top, SIZE
    if top >= SIZE - 1:
        # print("스택이 꽉 찼습니다. push를 수행할 수 없습니다.")
        return True
    return False


def is_stack_empty():
    global stack, top, SIZE
    if top == -1:
        # print("스택이 텅텅 비었습니다. pop을 수행할 수 없습니다.")
        return True
    return False


def push(data):
    global stack, SIZE, top
    if is_stack_full():
        return
    top += 1
    stack[top] = data


def pop():
    global stack, SIZE, top
    if is_stack_empty():
        return
    data = stack[top]
    stack[top] = None
    top = top -1
    return data


def peek():
    global stack, SIZE, top
    if is_stack_empty():
        print("현재 스택에 아무 자료도 없습니다.")
        return None
    print(stack[top])




if __name__ == "__main__" :
    urls = ["inha.ac.kr", "havard.edu", "yale.edu"]

    for url in urls:
        push(url)
        webbrowser.open("http://"+url)
        print(url, end = "-->")
        time.sleep(1)

    print("방문 종료")
    time.sleep(5)

    while True:
        url = pop()
        if url == None:
            break
        webbrowser.open("http://"+url)
        print(url, end = "-->")
        time.sleep(1)
    print("방문 종료")
