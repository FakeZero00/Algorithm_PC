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
    weights = heapdict.heapdict()
    weights[start_city_index] = 0, start_city_index
    completed = set()

    global mst
    mst = []
    while weights:
        ci, (w, fr) = weights.popitem()
        completed.add(ci)
        if(fr != ci): mst.append((fr, ci, w)) #시작 노드가 아니면 mst에 추가

        adjacents = graph[ci]
        for adj in adjacents:
            if adj in completed: continue
            weight = adjacents[adj]
            print(weights)
            if adj in weights:
                w = weights[adj][0]
            else: weights[adj] = weight, ci #인접한 점이 저장되어 있지 않다면 추가