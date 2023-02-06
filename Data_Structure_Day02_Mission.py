# Day02_Mission03
#마라톤 반환점 돌아오기

import random


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


SIZE = 10
stack = [None for i in range(SIZE)]
top = -1

if __name__ == "__main__" :
    spot_array = ["주안역", "학산소극장", "인하대 후문", "인하대 정문", "숭의역", "인하대 송도 캠퍼스"]
    random.shuffle(spot_array)
    count = 0
    print("반환점 가는길 :", end=" ")
    for spot in spot_array:
        push(spot)
        count += 1
        print(f'{spot} -->',end=" ")
    print("반환점")

    print("시작점 가는길 :", end=" ")
    while True:
        spot = pop()
        if spot:
            print(f'{spot} -->', end=" ")
        else:
            break
    print("시작점")
