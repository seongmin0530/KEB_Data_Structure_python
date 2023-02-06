# Day02_Mission03
#거꾸로 말해요


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


SIZE = 50
stack = [None for i in range(SIZE)]
top = -1

if __name__ == "__main__" :

    with open("거꾸로.txt","r", encoding='UTF8') as file:
        text = file.readlines()
        count = 0
        print("기존 단어 => ")
        for word in text:
            push(word)
            print(word,end = " ")

        print("\n거꾸로 => ")
        while True:
            word = pop()
            if word == None:
                break

            mstack = [None for i in range(len(word))]
            mtop = -1

            for c in word:
                mtop +=-1
                mstack[mtop] = c

            while True:
                if mtop == -1:
                    break
                c = mstack[mtop]
                mtop -= 1
                print(c, end = " ")

                #fail