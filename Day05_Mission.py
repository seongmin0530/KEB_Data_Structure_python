#Day05_Mission
# 진수 변환기


def transform(base, num):
    global number_chr
    if num < base:
        print(number_chr[num],end=" ")
    else:
        transform(base, num//base)
        print(num % base, end=' ')


def print_answer(base,num):
    print(f'{base}진수 변환 결과 :', end="")
    transform(base,num)
    print()


number_chr = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

if __name__ == "__main__" :
    num = int(input("10진수를 입력하세요.: "))
    print_answer(16,num)
    print_answer(8, num)
    print_answer(2, num)