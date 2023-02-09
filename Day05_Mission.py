#Day05_Mission
# 나이별 매칭(가장 나이가 많은 사람과 어린 사람 짝 지어주기)

def age_sort(array):
    for end in range(len(array)):
        for j in range(end,0,-1):
            if array[j-1][1]>array[j][1]:
                array[j-1][1], array[j][1] = array[j][1],array[j-1][1]
    sorted_array = array
    return array


def matching(array):
    end = -1
    for i in range(len(array)//2):
        print(f'{array[i][0]},{array[end][0]}')
        end -= 1


people_array = [["영미", 20], ["성민",25], ["철수",5], ["영희",8], ["옥자",70], ["형준",40]]

if __name__ == "__main__":
    sorted_array = age_sort(people_array)
    print(f'정렬결과 : {sorted_array}')
    matching(sorted_array)