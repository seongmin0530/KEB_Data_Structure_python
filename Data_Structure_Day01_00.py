# Data Structure_Day01_06
# 선형 리스트 ==>  통합


def insert_data(idx, pokemon):
    '''
    리스트의 특정 위치에 요소 삽입
    :param idx: 삽입할 위치, int
    :param pokemon: 삽입할 값, string
    :return: void
    '''
    if idx < 0 or idx > len(pokemons):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    pokemons.append(None)  # 빈칸 추가
    # pLen = len(pokemons)  # 배열의 현재 크기

    for i in range(len(pokemons) - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon  # 지정한 위치에 친구 추가


def delete_data(idx):
    '''
    리스트의 특정 위치에 있는 값 삭제
    :param idx: int
    :return: void
    '''
    if idx < 0 or idx > len(pokemons):
        print("Out of range!!!")
        return

    len_pokemons = len(pokemons)
    pokemons[idx] = None  # 데이터 삭제

    for i in range(idx + 1, len_pokemons):
        pokemons[i - 1] = pokemons[i]
        pokemons[i] = None  # 배열의 맨 마지막 위치 삭제

    pokemons.pop()  # == del (pokemons[len_pokemons - 1])


def Sdelete_data(idx):
    '''
    리스트의 특정 위치 이후에 있는 값 모두 삭제
    :param idx: int
    :return: void
    '''
    if idx < 0 or idx > len(pokemons):
        print("Out of range!!!")
        return

    len_pokemons = len(pokemons)
    count = 0

    for i in range(idx, len_pokemons):
        # del(pokemons[i])
        pokemons[i] = None  # 데이터 삭제
        count += 1

    for j in range(count):
        pokemons.pop()


def Sdelete_data_v02(idx):
    '''
    리스트의 특정 위치 이후에 있는 값 모두 삭제 다른 버전
    :param idx: int
    :return: void
    '''
    if idx < 0 or idx > len(pokemons):
        print("Out of range!!!")
        return

    len_pokemons = len(pokemons)
    count = 0

    for i in range(len_pokemons - idx):
        pokemons.pop()


def add_data(pokemon):
    '''
    리스트 맨뒤에 요소 추가
    :param pokemon: 입력할 데이터
    :return:
    '''
    pokemons.append(None)
    pokemons[len(pokemons)-1] = pokemon


pokemons = ["피카츄", "푸린", "파이리", "꼬부기", "롱스톤"]  #  기본 리스트 선언
menu = -1
if __name__ == "__main__":  # 해당 구문 밑에 있는 코드가 main처럼 동작

     while menu != 4:

        menu = input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> ")

        if (menu == '1'):
            data = input("추가할 데이터--> ")
            add_data(data)
            print(pokemons)
        elif (menu == '2'):
            pos = int(input("삽입할 위치--> "))
            data = input("추가할 데이터--> ")
            insert_data(pos, data)
            print(pokemons)
        elif (menu == '3'):
            pos = int(input("삭제할 위치--> "))
            delete_data(pos)
            print(pokemons)
        elif (menu == '4'):
            print(pokemons)
            #exit()  # 강제 중지
            break;
        else:
            print("1~4 중 하나를 입력하세요.")
            continue