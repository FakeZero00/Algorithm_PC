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
    weights = 