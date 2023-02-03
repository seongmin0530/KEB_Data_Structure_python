# Data Structure Mission01
talk = [['꼬부기',250],['피카츄',160],['롱스톤',50],['푸린',20],['이상해씨',10]]


def insert_data(idx, item):
    if idx < 0 or idx > len(talk):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    talk.append(None)  # 빈칸 추가
    # pLen = len(pokemons)  # 배열의 현재 크기

    for i in range(len(talk) - 1, idx, -1):
        talk[i] = talk[i - 1]
        talk[i - 1] = None
    talk[idx] = item


def insert_item(name, count):
    for i in range(len(talk)):
        if talk[i][1] < count:
            insert_data(i,[name,count])
            break


if __name__ == "__main__":
    name = input("이름을 입력하세요.: ")
    count = int(input("전투력을 입력하세요. :"))
    insert_item(name,count)
    print(talk)



