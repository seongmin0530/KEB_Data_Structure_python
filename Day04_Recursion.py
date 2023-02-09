# Day04_Recursion
# 자기자신을 반복해서 호출. 종료조건이 필요함.
# 재귀함수 ==> 호출 횟수가 많아 오버헤드 많이 발생, 따라서 Memoization과 같이 사용하여 오버헤드 줄일 수 있음

def fibo_rec(n) :
    """
    재귀함수 이용해 피보나치 수열 생성하는 함수
    :param n:n차항
    :return:(int)
    """
    global count_recursion
    count_recursion += 1
    if n <= 1:
        return n
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)


def fibo_iter(n):
    """
    반복문을 이용한 피보나치 수열 구하기
    :param n: n차항(int)
    :return: p1 = 계산결과 (int)
    """
    array = list()
    p1, p2 = 1, 1
    for _ in range(n):
        array.append(p1)
        p1,p2 = p2, p1+p2
    return array[-1]


def fibo_memo(n):
    """
    Memoization(DP)를 사용한 피보나치 수열 처리 함수
    :param n:
    :return:
    """
    global count_memoization, memo
    count_memoization += 1
    memo = [1, 1]
    if n <= 1:
        memo[n] = n
        return memo[n]

    else:
        for i in range(2,n+1):
            memo.append(memo[i-1] + memo[i-2])
        return memo[n]


memos = [None for _ in range (100)]     #전역 리스트
memos[0],memos[1] = 0,1
def fibo_memo_recu(n):
    """
    재귀함수 + memoization 이용해 피보나치 수열 구하는 함수
    :param n:
    :return:
    """
    global memos, cunt_memo_recu
    cunt_memo_recu += 1
    if n <= 1:
        return memos[n]

    if memos[n] is not None:        # 전역 메모리 memos에 이전에 계산한 결과값이 존재하면 메모리 값 리턴
        return memos[n]

    memos[n] = fibo_memo_recu(n-2) + fibo_memo_recu(n-1)    # 처음 방문하는 n이면 재귀함수
    return memos[n]


memo = list()
count_memoization = 0
count_recursion = 0
cunt_memo_recu = 0

if __name__ == "__main__":
    # 피보나치 구현 함수 성능 분석
    # ***********************************************************************************
    # print ('피보나치 수열\n 0 1')
    # for i in range(2, 30):
    #     print(f'{i} : {fibo_rec(i)}')  # recursion
    #     # print(f'{i} : {fibo_iter(i)}')  # repetition
    #     print(f'{i} : {fibo_memo(i)}')  # memoization
    #     print(f'{i} : {fibo_memo_recu(i)}')  # memoization + recursion
    # print(f'재귀{count_recursion}, 메모{count_memoization}, 재귀메모{cunt_memo_recu}')
    # ***********************************************************************************

