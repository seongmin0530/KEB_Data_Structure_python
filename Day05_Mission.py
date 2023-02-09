# Day05_Mission
# 큌정렬 실행시간 확인

import random
import time

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
    return array


data_array = [random.randint(0,1000000) for _ in range(1000000)]

if __name__ == "__main__":
    data_array.sort()
    position = random.randint(0,len(data_array))
    data = data_array[-1]
    data_array.insert(position,data)
    start = time.time()
    quick_sort(data_array)
    end = time.time()
    print(f'{data} 데이터가 {position}위치에 삽입되었습니다.')
    print(f'재정렬 완료. 소요시간:{(end-start):.2f}')