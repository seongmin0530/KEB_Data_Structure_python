# Data Structure_Day01_08
# 선형 리스트 ==>  특수 다항식 처리 프로그램

# 차수가 매우 큰 다항식을 처리할 때 for문을 이용해 작성하면
# 리스트 공간 낭비가 심하므로 새로운 리스트를 만들어 계수가 있는 차수 정보를 저장


def print_poly(tx, px):
    poly_str = "P(x) = "

    for i in range(len(px)):
        term = tx[i]  # 항 차수
        coef = px[i]  # 계수

        if (coef >= 0):
            poly_str += "+"
        poly_str += f'{coef}x^{term}'

    return poly_str


def calc_poly(xVal, tx, px):
    ret_value = 0

    for i in range(len(px)):
        term = tx[i]
        coef = px[i]
        ret_value += coef * x_value ** term

    return ret_value


px = [7, -4, 5]
tx = [300, 20, 0]


if __name__ == "__main__":
    print(print_poly(tx, px))

    x_value = int(input("X 값을 입력하세요.: "))

    print(calc_poly(x_value, tx, px))

