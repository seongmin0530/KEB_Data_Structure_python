# graph의 응용
# ==> 최소 비용 신장 트리(최단경로 알고리즘)

# 신장 그래프 ==> 최소 간선으로 모든 정점이 연결되는 그래프
# 신장 트리 ==> 최소 간선으로 모든 정점이 연결되는 트리(에지 개수 = 정점 - 1개) == 그래프에서 모든 정점을 탐색하는 경로(여러가지가 존재)
# 가중치 그래프 ==> edge에 가중치가 있는 그래프

# 최소 비용 신장트리(Minimum Cost Spanning Tree) ==> 가중치 그래프에서 만들 수 있는 신장 트리 중 가중치의 합계가 최소인 트리
# ==> 구현 알고리즘 : 프림(prim)알고리즘, 크루스칼(Kruskal)알고리즘

from operator import itemgetter     # sorted 사용 위해 import


class Graph():
    def __init__(self,size):
        self.SIZE = size
        self.graph = [[0 for i in range(size)] for j in range(size)]


def make_graph():
    """
    그래프 만드는 함수
    :return:
    """
    G1 = Graph(6)

    Ablock, Bblock, Cblock, Dblock, Eblock, Fblock = 0, 1, 2, 3, 4, 5
    G1.graph[Ablock][Bblock] = 80; G1.graph[Ablock][Dblock] = 10;
    G1.graph[Bblock][Ablock] = 80; G1.graph[Bblock][Dblock] = 40; G1.graph[Bblock][Eblock] = 70;
    G1.graph[Cblock][Eblock] = 30; G1.graph[Cblock][Fblock] = 60
    G1.graph[Dblock][Ablock] = 10; G1.graph[Dblock][Bblock] = 40; G1.graph[Dblock][Eblock] = 50;
    G1.graph[Eblock][Bblock] = 70; G1.graph[Eblock][Dblock] = 50; G1.graph[Eblock][Cblock] = 30; G1.graph[Eblock][Fblock] = 20
    G1.graph[Fblock][Eblock] = 20; G1.graph[Fblock][Cblock] = 60
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


def find_vertex(g,find_vertex):
    """
    깊이 우선 탐색 기반으로 방문하지 않은 정점(그래프와 떨어진 정점)이 있는지 확인하는 함수
    :param g: 그래프
    :param find_vertex: 확인할 정점
    :return:
    """
    stack = []
    visit_array = []                                # 방문한 정점

    current = 0                                     # 현재 확인할 정점
    stack.append(current)                           # 확인할 정점을 스택에 추가
    visit_array.append(current)                     # 방문 목록에 현재 정점 추가

    while len(stack)!=0 :                           # 확인할 정점의 모임(stack)이 비어있기 전까지
        next_point = None                           #
        for vertex in range(g.SIZE):                # 그래프만큼 반복
            if g.graph[current][vertex] != 0:       # 만약 해당 에지가 연결되어 있다면
                if vertex in visit_array:           # 1) 그리고 방문 목록에 있다면 pass
                    pass
                else:                               # 2) 그리고 방문 목록에 없다면 다음 정점으로 지정
                    next_point = vertex
                    break
        if next_point is not None:                  # 다음 방문할 정점이 있을 때
            current = next_point                    # 현재 확인할 정점 <= 다음 방문할 정점
            stack.append(current)                   # 확인할 정점의 모임(stack)에 현재 확인할 정점 추가
            visit_array.append(current)             # 방문 목록에 현재 확인할 정점 추가

        else:                                       # 다음에 방문할 정점이 없을 때
            current = stack.pop()                   # 현재 확인할 정점을 이전에 확인한 정점으로 이동

    if find_vertex in visit_array:                  # 만약 찾고자 하는 정점이 그래프와 연결되어 있다면(방문 했다면)
        return True                                 # True 반환
    else:                                           # 만약 찾고자 하는 정점이 그래프와 연결되어 있지 않다면(방문하지 않았다면)
        return False                                # False 반환

G1 = make_graph()
if __name__ == "__main__":
    print("아파트 단지 최단 거리 순찰로")
    print("인접행렬")
    print_graph(G1)

    edge_array = []                     # 간선의 목록
    for row in range (G1.SIZE):
        for col in range(G1.SIZE):
            if G1.graph[row][col] != 0:
                edge_array.append([G1.graph[row][col], row, col])

    edge_array = sorted(edge_array, key=itemgetter(0), reverse=True)  # edge_array의 가중치를 기준으로 오름차순 정렬

    re_array = []                           # 중복 간선 제거
    for i in range(0,len(edge_array), 2):   # 2개 간격으로 추출하면 같은 종류의 간선 제거할 수 있음(정렬되어있다는 가정하에)
        re_array.append(edge_array[i])

    index = 0
    while(len(re_array) > G1.SIZE-1):       # 간선의 개수 = 정점개수 - 1일 때(신장 트리가 될 때)까지 반복
        save_cost = re_array[index][0]      # 간선의 가중치(제거후 동떨어진 정점이 발생했을 때 간선 복구를 위해 미리 저장)
        start = re_array[index][1]          # 출발점
        end = re_array[index][2]            # 도착점

        G1.graph[start][end] = 0            # 간선 제거
        G1.graph[end][start] = 0            # 간선 제거 (위 간선과 동일한 간선)

        start_point = find_vertex(G1,start) # 제거한 간선의 출발점이 그래프와 동떨어져 있는지 확인
        end_point = find_vertex(G1,end)     # 제거한 간선의 도착점이 그래프와 동떨어져 있는지 확인

        if start_point and end_point:       # 만약 출발점/도착점이 모두 그래프와 동떨어져 있지 않다면
            del(re_array[index])            # 해당 노드 목록 삭제
        else:                               # 둘 중 하나라도 그래프와 동떨어진다면
            G1.graph[start][end] = save_cost    # 복구
            G1.graph[end][start] = save_cost    # 복구
            index += 1

    print("효율적인 아파트 단지 순찰로")
    print_graph(G1)


# 프로세스
# 1. 그래프 생성
# 2. [[가중치, 출발지,도착지][가중치,출발지, 도착지]] 형태의 가중치 목록 생성 ==> edge_array
# 3. 증복되는 간선 삭제(가중치 목록 sorted이용) ==> sort : 원본 수정, sorted : 수정된 결과 반환, 원본 그대로 ==> re_array
# 4. 모든 도시가 연결될 수 있는 한에서 가중치가 큰 간선부터 인접행렬에서 제거
# 5. 출발점과 도착점이 각각 그래프와 동떨어져 있는지 확인 ==> find_vertex
# 6. 둘 중 하나라도 동떨어져 있다면 인접 행렬 복구
# 7. 둘 다 동떨어져 있지 않다면 간선 목록에서 최종 삭제
# (인접행렬 삭제 -> 확인 -> 인접행렬 복구) or (인접행렬 삭제 -> 확인 -> re_array 삭제)