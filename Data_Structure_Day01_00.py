# Data Structure_Day01_07
# 선형 리스트 ==>  다항식의 선형 리스트 표현과 계산 프로그램


def print_Poly(px):
    """
    다항식 출력 함수
    :param px: list(계수가 담겨있는 리스트)
    :return: String(출력할 문자열)
    """
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1
    poly_str = "P(x) = "

    for i in range(len(px)):
        coef = px[i]  # 계수

        if coef > 0 and i != 0:
            poly_str = poly_str + "+"

        elif coef == 0:
            term = term - 1
            continue

        poly_str = poly_str +f'{coef}x^{term} '
        term -= 1

    return poly_str


def calc_Poly(x_Val, px):
    """
    다항식 계산 함수
    :param x_Val:int(x값)
    :param px:inst(계수)
    :return:int(계산결과)
    """
    return_val = 0
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1

    for i in range(len(px)):
        coef = px[i]  # 계수
        return_val += coef * x_value ** term
        term -= 1

    return return_val


px = [7, -4, 0, 5]

if __name__ == "__main__":
    print(print_Poly(px))
    x_value = int(input("X 값 : "))
    print(calc_Poly(x_value, px))

