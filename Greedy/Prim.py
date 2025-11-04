from data_city import City, five_letter_cities, make_edges
import data_sample_cities as dsc
import heapdict

cities = five_letter_cities[dsc.data_sets[0]['beg'] : dsc.data_sets[0]['end']]
edges = dsc.data_sets[0]['edges']

def build_graph():
    global graph
    graph = {u: dict() for u in range(n_cities)}
    for u,v,w in edges:
        graph[u][v] = w
        graph[v][u] = w
    print(graph)

if __name__ == '__main__':
    global n_cities

    n_cities = len(cities)
    build_graph()

    start_city_index = 0
    global weights, completed
    weights = heapdict.heapdict()   #도시 인덱스를 키로, (가중치, 출발도시인덱스) 를 값으로 저장한 최소 힙 구조(가중치를 기준으로 자동으로 최소힙 구성)
    weights[start_city_index] = 0, start_city_index # weight, from
    completed = set()

    global mst
    mst = []
    while weights:
        ci, (w, fr) = weights.popitem() # ci: 시작 city이름 키로 사용, w: 가중치, fr: 도착 city
        completed.add(ci)   #내륙 집합에 점 추가
        if(fr != ci): mst.append((fr, ci, w)) #시작 노드가 아니면 mst에 추가

        adjacents = graph[ci] #현재 점의 인접한 점들
        for adj in adjacents:   #인접한 점들 하나씩 adj에 넣기
            if adj in completed: continue   #인접한 점이 이미 내륙에 있으면 continue
            weight = adjacents[adj]     #인접한 점까지의 가중치
            if adj in weights:  #인접한 점이 이미 weights 힙 안에 저장되어 있는지 확인(내륙에 있는지 없는지)
                w = weights[adj][0] #이미 저장되어 있는 가중치 확인
                if weight < w:
                    weights[adj] = weight, ci
            else: weights[adj] = weight, ci #인접한 점이 저장되어 있지 않다면 추가

        if len(mst) >= n_cities -1: break

    print(mst)