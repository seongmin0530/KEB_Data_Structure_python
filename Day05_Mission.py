# Day05_Mission
# 교실에 있는 학생중 중간 성적을 가진 학생 찾기

def sort(array):
    for end in range(len(array)):
        for j in range(end,0,-1):
            if array[j-1]>array[j]:
                array[j-1], array[j] = array[j],array[j-1]
    sorted_array = array
    return array


def make_array(array):
    result_array = list()
    for i in range(len(array)):
        for j in range(len(array[i])):
            result_array.append(array[i][j])
    return result_array


def find_middle(array):
    print(array[len(array)//2])


people_array = [[20,35,40,90],
                [47,62,79,30],
                [10,43,72,59],
                [5,26,65,87]]


if __name__ == "__main__":

   sorted_array = sort(make_array(people_array))
   print(sorted_array)
   find_middle(sorted_array)