# stack의 응용 ==> 올바른 괄호 짝 찾기
# 1. 닫는 괄호를 만났을 때 스택은 비어있지 않아야 함
# 2. 닫는 관호를 만났을 때 추출한 괄호는 여는 괄호여야 함.
# 3. 2번을 만족함과 동시에 괄호의 종류가 같아야 함.
# 4. 모든 수식을 처리하고 나면 스택은 비어있어야 함


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


def check_bracket(expr):
    """
    괄호의 짝이 맞지 않으면 False를 반환하는 함수
    :param expr: 괄호를 포함한 수식 (chr)
    :return: True/False (bool)
    """
    for ch in expr:         # 수식에서 글자 추출하여 반복
        if ch in '([{<':        # 수식 안에서 여는 괄호가 있으면
            push(ch)            # 해당 괄호 push
        elif ch in ')]}>':      # 수식 안에서 닫는 괄호가 있으면
            out = pop()         # 해당 괄호 pop
            if ch == ')' and out == '(':    # 괄호가 )(, ][, }{, >< 형태일 때 패스
                pass
            elif ch == ']' and out == '[':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == '>' and out == '<':
                pass
            else:
                return False
        else:       # 괄호가 아닌 문자 ==> pass
            pass
    return is_stack_empty()


SIZE = 50
stack = [None for i in range(SIZE)]
top = - 1

if __name__ == "__main__" :
    data_array = ["(2*[3+1])","(A+B)",")A+B(","((A+B)-C", "(A+B]"]
    for expr in data_array:
        top = -1
        print(expr, ' : ', check_bracket(expr))
