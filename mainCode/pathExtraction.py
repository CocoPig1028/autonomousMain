import heapq  # 우선순위 큐 구현

def dijkstra(graph, start, parents):
    distances = {node: int(1e9) for node in graph}  # 처음 초기값은 무한대
    distances[start] = 0  # 시작 노드까지의 거리는 0
    queue = []
    heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작

    while queue:  # queue에 남아있는 노드가 없을 때까지 탐색
        dist, node = heapq.heappop(queue)  # 탐색할 노드, 거리

        # 기존 최단거리보다 멀다면 무시
        if distances[node] < dist:
            continue

        # 노드와 연결된 인접노드 탐색
        for next_node, next_dist in graph[node].items():
            distance = dist + next_dist  # 인접노드까지의 거리
            if distance < distances[next_node]:  # 기존 거리 보다 짧으면 갱신
                distances[next_node] = distance
                parents[next_node] = node  # 이전 노드 저장
                heapq.heappush(queue, [distance, next_node])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    return distances

#노드 간 가중치 정보 딕셔너리

def pathExtraction() :
    graph = {
        1 : {6 : 0},
        2 : {7 : 0},
        3 : {8 : 0},
        5 : {6 : 0},
        6 : {1 : 0, 5 : 0, 7 : 0, 11 : 0},
        7 : {2 : 0, 6 : 0, 8 : 0, 12 : 0},
        8 : {3 : 0, 7 : 0, 9 : 0, 13 : 0},
        9 : {8 : 0},
        10 : {11 : 0},
        11 : {6 : 0, 10 : 0, 12 : 0, 16 : 0},
        12 : {7 : 0, 11 : 0, 13 : 0, 17 : 0},
        13 : {8 : 0, 12 :0, 14 : 0, 18 : 0},
        14 : {13 : 0},
        15 : {16 : 0},
        16 : {11 : 0, 15 : 0, 17 : 0, 21 : 0},
        17 : {12 : 0, 16 : 0, 18 : 0, 22 : 0},
        18 : {13 : 0, 17 : 0, 19 : 0, 23 : 0},
        19 : {18  : 0},
        21 : {16 : 0},
        22 : {19 : 0},
        23 : {18 : 0}
    }

    #단위시간 별 가중치 수정 함수 구현해야함

    # changeWeightNum = int(input("가중치를 수정할 노드 번호 : "))
    # changeWeight = int(input("가중치 : "))

    #가중치 수정 부분 (나중에 함수화 하기)
    # for i in graph:
    #     if changeWeightNum in graph[i]:
    #         graph[i][changeWeightNum] = changeWeight
    #         print(graph)

    #노드 저장 딕셔너리
    parents = {i : 0 for i in graph}

    #출발지 도착지 노드 설정 (나중에 함수화)
    start = int(input("출발 노드 입력 : "))
    #모든 경로 출력 (가중치 영향 X)
    print(dijkstra(graph, start, parents))
    path = []
    curr = int(input("도착 노드 입력 : "))
    while curr:
        path.append(curr)
        curr = parents[curr]
    
    print(path[::-1])
    return path[::-1]
    
