# Data Structure_Day01_05
# 선형 리스트 ==>  + 선택한 데이터 이후의 데이터 모두 지우기 v02


def insert_data(idx, pokemon):
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
    if idx < 0 or idx > len(pokemons):
        print("Out of range!!!")
        return

    len_pokemons = len(pokemons)
    count = 0

    for i in range(len_pokemons - idx):
        pokemons.pop()


if __name__ == "__main__":  # 해당 구문 밑에 있는 코드가 main처럼 동작
    pokemons = ["피카츄", "푸린", "파이리", "꼬부기", "롱스톤"]  # main에서 기본 리스트 선언

    # data insert
    insert_data(2, '디아루가')
    print(pokemons)
    insert_data(6, '펄기아')
    print(pokemons)

    # data delete
    delete_data(1)
    print(pokemons)
    delete_data(3)
    print(pokemons)

    # 선택한 인덱스
    Sdelete_data(1)
    print(pokemons)
    Sdelete_data(3)
    print(pokemons)
