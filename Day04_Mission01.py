# Day04_Mission01
# 관광 루트중 관광객이 제일 많은 명소 찾기

class Graph():
    def __init__(self,size):
        self.SIZE = size
        self.graph = [[0 for i in range(size)] for j in range(size)]


def make_graph():
    """
    그래프 만드는 함수
    :return:
    """
    global tourist_array
    G1 = Graph(5)

    Mt_Hanlla, udo_island, Geum_Oreum, Manjanggul_cave, dragon_head_rock= 0, 1, 2, 3, 4
    G1.graph[Mt_Hanlla][udo_island] = 1; G1.graph[Mt_Hanlla][Geum_Oreum] = 1;
    G1.graph[udo_island][Mt_Hanlla] = 1; G1.graph[udo_island][Geum_Oreum] = 1; G1.graph[udo_island][Manjanggul_cave] = 1;
    G1.graph[Geum_Oreum][Mt_Hanlla] = 1; G1.graph[Geum_Oreum][udo_island] = 1; G1.graph[Geum_Oreum][Manjanggul_cave] = 1;
    G1.graph[Manjanggul_cave][dragon_head_rock] = 1; G1.graph[Manjanggul_cave][udo_island] = 1; G1.graph[Manjanggul_cave][Geum_Oreum] = 1;
    G1.graph[dragon_head_rock][Manjanggul_cave] = 1;

    tourist_array = [['Mt_Hanlla',300], ['udo_island',600], ['Geum_Oreum',100], ['Manjanggul_cave',900], ['dragon_head_rock',400]]
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


def dfs(g,tourist_array):
    """
    깊이 우선 탐색 기반으로 방문하지 않은 정점(그래프와 떨어진 정점)이 있는지 확인하는 함수 + 최대 관광객을 가진 명소/관광객 반환
    :param g: 그래프
    :param find_vertex: 확인할 정점
    :return: 최대 관광객을 가진 명소(int)
    """

    stack = []
    visit_array = []                                # 방문한 정점

    current = 0                                     # 현재 확인할 정점
    max_place = current                             # 광광객이 제일 많은 장소
    max_tourist = tourist_array[current][1]         # 해당 장소의 관광객

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

            if tourist_array[current][1] > max_tourist:                        # ==> 현재 방문한 관광지의 관광객이 max_tourist보다 많다면
                max_tourist = tourist_array[current][1]                        # ==> 현재 방문한 관광지의 관광객 => max_tourist
                max_place = current                                            # ==> 가장 많은 관광객이 있는 장소 <= 현재 방문한 장소

        else:                                       # 다음에 방문할 정점이 없을 때
            current = stack.pop()                   # 현재 확인할 정점을 이전에 확인한 정점으로 이동
    return max_place


tourist_array = None

if __name__ == "__main__" :
    G1 = make_graph()
    max_place = dfs(G1, tourist_array)
    print_graph(G1)
    print(f'관광지가 가장 많은 명소(관광객) : {tourist_array[max_place][0]},{tourist_array[max_place][1]}')

