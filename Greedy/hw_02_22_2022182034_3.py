edges=[
    (0, 2, 267), (0, 10, 292), (0, 14, 162), (0, 17, 311), (0, 23, 281), 
    (1, 11, 331), (1, 19, 307), (1, 22, 395), (2, 6, 256), (2, 10, 319), 
    (2, 14, 111), (2, 16, 316), (2, 18, 405), (2, 20, 451), (2, 21, 415), 
    (2, 24, 488), (3, 8, 249), (3, 12, 438), (3, 15, 84), (4, 7, 445), 
    (4, 10, 53), (4, 16, 320), (4, 17, 135), (4, 20, 229), (4, 24, 298), 
    (5, 9, 367), (5, 13, 483), (5, 15, 261), (5, 19, 358), (6, 7, 109), 
    (6, 12, 358), (6, 14, 319), (6, 16, 456), (6, 18, 153), (6, 21, 465), 
    (7, 12, 440), (7, 13, 465), (7, 14, 210), (7, 23, 236), (8, 9, 106), 
    (10, 16, 285), (11, 13, 371), (11, 19, 53), (12, 13, 243), (12, 18, 364), 
    (12, 21, 395), (12, 22, 442), (13, 21, 170), (14, 18, 451), (14, 23, 318),
    (16, 17, 287), (16, 23, 325), (17, 24, 392), (19, 22, 146), (20, 24, 76)
]
from heapdict import heapdict
num_vertex = 25

g = {i:dict() for i in range(num_vertex)}
for u, v, w in edges:
    g[u][v] = w
    g[v][u] = w
mst = []

def append(s, e, w):
    if s <= e:
        mst.append((s,e,w))
    else:
        mst.append((e,s,w))
    mst.sort(key=lambda e:e[0]*1000+e[1])

origins = dict()

def dijkstra(start):
    D = heapdict() #key 종착점
    D[start] = 0, start
    completed = set()
    global origins
    origins[start] = start
    current_origin = start
    while D:
        i_to, (weight, i_from) = D.popitem()
        completed.add(i_to)
        current_origin = i_from

        if i_from != i_to:
            append(i_from, i_to, weight)
            origins[i_to] = current_origin

        for adj_i, adj_w in g[i_to].items():
            if adj_i in completed: continue
            wa = weight + adj_w
            if adj_i not in D or wa < D[adj_i][0]:
                D[adj_i] = wa, i_to

path = [[] for _ in range(num_vertex)]
weight_values = []

def find_root(v, index):
    if v == origins[v]:
        path[index].append(v)
        return
    else:
        path[index].append(v)
        find_root(origins[v], index)

def print_path(v, start):
    find_root(v, v)
    weight_value = 0
    for i in range(len(path[v]) - 1):
        if path[v][i] == start: break
        weight_value += g[path[v][i]][path[v][i+1]]
    weight_values.append((v, weight_value))
    print(f'Vertex {v} : ' + ' -> '.join(map(str, reversed(path[v]))) + f' (Weight: {weight_value})')
    
result = dijkstra(12)
origins = dict(sorted(origins.items()))
for i in range(num_vertex):
    print_path(i, 12)
print(mst)