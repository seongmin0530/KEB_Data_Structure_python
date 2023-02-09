# Day05_Sort
# 1. 선택정렬 ==> 데이터 중 가장 작은/큰 값을 뽑는 동작 반복 (넘어감)
# 2. 삽입정렬 ==> 데이터별로 삽입될 위치를 찾아 삽입하는 방식
# [(find_insert_idx + select_sorting 이용) = 성능 low(메모리 낭비), => insertion_sort 사용] ==>데이터가 작을 때 유용


# 고급 정렬
# 1. 버블 정렬(넘어감)
# 2. 퀵 정렬 ==> 기준점 선택 후 그 기준점보다 큰수/작은수로 나누어 정렬, 반복 ==> 피벗값이 중앙이 아니라 양쪼 끝값에 잡히면 성능이 급감함


import random


def insertion_sort(array):
    """
    삽입 정렬 구현
    :param array:
    :return:
    """
    n = len(array)
    for end in range(1,n):                                                                  # 새로운 데이터와  삽입 사이클
        for cur in range(end, 0, -1):                                                       # 삽입 완료된 데이터 리스트안에서의 순차적 비교 사이클
            if array[cur-1] > array[cur]:                   # (> 오름 차순), (< 내림 차순)
                array[cur-1], array[cur] = array[cur], array[cur-1]
    sorted_array = array
    print(sorted_array)


def q_sort(array,start,end):
    if end <= start:
        return

    low = start
    high = end

    pivot = array[(low + high) // 2]            # 1. 중간지점 잡기
    while low <= high:                  # 2. Low가 High가 같아질 때까지 반복
        while array[low] < pivot:               # 3-1. Low값이 pivot보다 작을때 까지              # (< 올림차순)/(> 내림차순)
            low += 1                                # 4-1. Low자리 증가
        while array[high] > pivot:              # 3-2. High값이 pivot보다 클 때까지               # (> 올림차순)/(<내림차순)
            high -= 1                               # 4-2. High값 감소
        if low <= high:                         # 3. low값이 High값보다 작으면
            array[low], array[high] = array[high], array[low]
            low,high = low + 1, high - 1            # 4. 해당 위치의 Low/High값을 교환하고 Low값과 High값 증가,감소시킴

    mid = low                                   # 5. Low값을 middle값으로 설정

    q_sort(array, start, mid-1)                 # 6. pivot 기준 왼쪽 배열 sorting by 재귀호출
    q_sort(array, mid, end)                     # 6. pivot 기준 오른쪽 배열 sorting by 재귀호출


def quick_sort(array):                          # 주어진 배열을 이용해 q_sorting 호출하는 최종 함수
    q_sort(array,0,len(array)-1)
    print(array)



before_array = [random.randint(0,200) for _ in range(20)]   #리스트 컴프리헨션


if __name__ == "__main__":
    # insertion_sort(before_array)
    quick_sort(before_array)
