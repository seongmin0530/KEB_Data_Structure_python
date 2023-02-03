# Data Structure_Day01_01
# 선형 리스트

pokemons = list()  # 빈 배열


def add_data(pokemon):
    pokemons.append(None)
    # pokemons[len(pokemons) - 1] = pokemon  # 배열의 최대 범위를 넘어지 않기 위해
    pokemons[-1] = pokemon


add_data('피카츄')
add_data('푸린')
add_data('파이리')
add_data('꼬부기')
add_data('롱스톤')


print(pokemons)