# day04_graph
# 여러 노드가 서로 연결된 구조 ==> 여러 노드가 연결되어있을 수 있음(tree와의 차이점)
# 노드 = 정점(Vertex), 에지(Edge) ==> graph(G) = V와 E의 집합
# graph 종류 = 방향 그래프, 무방향 그래프
# 무방향 그래프   : 간선 ==> (A, B) --> (A, B) == (B, A)
# 방향 그래프    : 간선 ==> <A, B> --> <A, B> != <B, A>
# 가중치 그래프 : E마다 가중치가 다르게 부여된 그래프

# 그래프의 모든 V 한번씩 방문하는 법 = 깊이 우선 탐색(Depth First Search = DFS), 너비우선 탐색(Breadth First Search = BFS)
# DFS : stack 이용 (아래로 파고드는 개념)
# 리스트 메서드 .append(), .pop() 이용하여 stack 구현없이 사용 ==> [len()이용하여 스택 길이 확인. if 스택길이 = 0--> empty]
# DFS ==> 나의 팔로워중 한명 선택 => 나의 팔로워의 팔로워 중 한명 탐색~~~

# BFS : queue 이용(레벨별로 탐색하는 개념)
# deque 메서드 .append(), .popleft()이용하여 queue 구현없이 사용 ==>그냥 queue.pop(0)을 사용하면 pop후 데이터를 옮기는 과정에서 OVERHEAD 발생
# BFS ==> sns와 유사. 나의 팔로워 전부 탐색 -> 나의 팔로워의 팔로워 전부 탐색~~~

# graph의 인접 행렬 표현 : 코드에서 graph를 구현하는 방법
# ==> 1. 정점개수 * 정점개수 size의 행렬 생성
# ==> 2. 왼쪽 = 출발점, 위쪽 = 도착점
# ==> 2. 출발점과 도착점이 같은 자기자신 = 0
# ==> 3. 두 정점(출발점, 도착점)이 연결된 경우 1, 연결되지 않은 경우 0
# 인접행렬에 주석(Vertex 이름)을 추가하면 더 직관적으로 볼 수 있음
# 무방향 그래프 ==> 인접행렬의 대각선을 기준으로 서로 대칭되는 특성(방향 그래프는 없음)


from collections import deque # deque 사용 위해 import(for BFS)


class Graph():
    def __init__(self,size):
        self.SIZE = size
        self.graph = [[0 for i in range(size)] for j in range(size)]


def make_graph():
    """
    그래프 만드는 함수
    :return:
    """
    G1 = Graph(9)

    A, B, C, D, E, F, G, H, I = 0, 1, 2, 3, 4, 5, 6, 7, 8
    G1.graph[A][B] = 1; G1.graph[A][C] = 1; G1.graph[A][E] = 1  # 간선을 손수 이어주는 부분(변수 = 인덱스를 통해 노드 이름을 직관적으로 대입할 수 있음)
    G1.graph[B][A] = 1; G1.graph[B][C] = 1; G1.graph[B][D] = 1
    G1.graph[C][A] = 1; G1.graph[C][B] = 1; G1.graph[C][D] = 1; G1.graph[C][E] = 1; G1.graph[C][F] = 1
    G1.graph[D][B] = 1; G1.graph[D][C] = 1
    G1.graph[E][H] = 1; G1.graph[E][C] = 1; G1.graph[E][G] = 1; G1.graph[E][A] = 1
    G1.graph[F][C] = 1
    G1.graph[G][E] = 1; G1.graph[G][I] = 1
    G1.graph[H][E] = 1; G1.graph[H][I] = 1
    G1.graph[I][G] = 1; G1.graph[I][H] = 1
    return G1


def print_graph(g):
    """
    인점행렬 출력하기
    :return:
    """
    G1 = g
    make_graph()
    # node_array = ["A", "B", "C", "D"]  # 주석(노드 이름) 출력 구문
    # print(" ", end=" ")
    # for node in node_array:
    #     print(node, end=" ")
    # print()

    for row in range(G1.SIZE):  # 인접 행렬 출력문
        # print(f'{node_array[row]}', end=" ")
        for col in range(G1.SIZE):
            print(G1.graph[row][col], end=" ")
        print()


def dfs(g):
    """
    깊이 우선 탐색(dfs)구현(문제 있으므로 확인 필요)
    :return:
    """
    global stack, visit_array
    G1 = g
    make_graph()

    current = 0  # 현재 정점                      ==> start vertex 방문
    stack.append(current)  # 현재 정점을 stack에 추가
    visit_array.append(current)  # 현재 정점을 방문 리스트에 추가

    while len(stack) != 0:  # 스택이 비어있지 않다면
        next_point = None  # 현재 vertex와 연결된 vertex = next_point

        for vertex in range(G1.SIZE):  # 모든 정점을 확인
            if G1.graph[current][vertex] == 1:  # graph의 current와 vertex가 연결 되어 있다면
                if vertex in visit_array:  # 그리고 해당 vertex를 방문한 적이 있다면 pass
                    pass
                else:  # 그리고 해당 vertex를 방문한 적이 없다면
                    next_point = vertex  # 현재 vertex와 연결된 vertex 정보를 저장(연결된 vertex) == 다음 정점으로 지정
                    break

        if next_point is not None:  # 연결된 정점이 있다면(다음에 방문할 정점이 있다면)
            current = next_point  # 현재 vertex를 앞서 저장한 (연결된 vertex)로 지정
            stack.append(current)  # stack에 현재 vertex를 추가
            visit_array.append(current)  # 방문 리스트에 현재 vertex를 추가

        else:  # 연결된 정점이 없다면(다음에 방문할 정점이 없다면)
            current = stack.pop()  # 되돌아오기

    # 스택이 빌 때까지 -> 1. 다음 정점이 방문한 적 있는지 확인, 2. 없다면 스택과 방문 내역에 추가 3. 있으면 넘어가기 4. 방문할 정점 없으면 POP하여 시작지점으로 돌아오기

    print("dfs 탐색 루트 : ", end=" ")
    for visit in visit_array:
        print(chr(ord('A') + visit), end=" --> ")
    print("END")
# 문제 있으니 코드 확인 후 git에 업로드 할 것

def bfs(g):
    global visit_array, queue
    G1 = g
    current = 0
    queue.append(current)  # enqueue
    visit_array.append(current)

    while len(queue) != 0:
        next_point = None
        for vertex in range(G1.SIZE):
            if G1.graph[current][vertex] == 1:
                if vertex in visit_array:
                    pass
                else:
                    next_point = vertex
                    break

        if next_point is not None:
            current = next_point
            queue.append(current)  # enqueue
            visit_array.append(current)
        else:
            # current = queue.pop(0)  # O(n), OVERHEAD
            current = queue.popleft()  # O(1), dequeue ==> deque의 popleft()를 이용하여 que와 같은 자료구조 형태 갖춤

    print("bfs 탐색 루트 : ", end=" ")
    for visit in visit_array:
        # print( chr(ord("A")+visit), end=' --> ')
        print(chr(ord("A")+visit), end=' --> ')
    print("END")
# 문제 있으니 코드 확인 후 git에 업로드 할 것

stack = []              # for DFS
queue= deque([])        # for BFS
visit_array = []        # for DFS/BFS

if __name__ == "__main__":
    dfs(make_graph())

