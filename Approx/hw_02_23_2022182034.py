from heapdict import heapdict

edges = [
    (0, 2, 267), (0, 10, 292), (0, 14, 162), (0, 17, 311), (0, 23, 281),
    (1, 11, 331), (1, 19, 307), (1, 22, 395),
    (2, 6, 256), (2, 10, 319), (2, 14, 111), (2, 16, 316), (2, 18, 405), (2, 20, 451), (2, 21, 415), (2, 24, 488),
    (3, 8, 249), (3, 12, 438), (3, 15, 84),
    (4, 7, 445), (4, 10, 53), (4, 16, 320), (4, 17, 135), (4, 20, 229), (4, 24, 298),
    (5, 9, 367), (5, 13, 483), (5, 15, 261), (5, 19, 358),
    (6, 7, 109), (6, 12, 358), (6, 14, 319), (6, 16, 456), (6, 18, 153), (6, 21, 465),
    (7, 12, 440), (7, 13, 465), (7, 14, 210), (7, 23, 236),
    (8, 9, 106),
    (10, 16, 285),
    (11, 13, 371), (11, 19, 53),
    (12, 13, 243), (12, 18, 364), (12, 21, 395), (12, 22, 442),
    (13, 21, 170),
    (14, 18, 451), (14, 23, 318),
    (16, 17, 287), (16, 23, 325),
    (17, 24, 392),
    (19, 22, 146),
    (20, 24, 76)
]
num_vertex = 25

start = 12

#dict형 출력 함수
# def print_dict(d):
#     for k, v in d.items():
#         print(f'{k}: {v}')

#=============Graph 생성===============
#u = 시작점, v = 도착점
g = {u:dict() for u in range(num_vertex)}
for u, v, w in edges:
    g[u][v] = w
    g[v][u] = w

# print("Edge List 전부 출력:")
# print_dict(g)

#=================MST 생성 (Prim)================
D = heapdict() #key = u(도착점), value = (w, v(시작점))
comp = set() #내륙 확인용 집합
mst = [] #MST 결과 edge list

D[start] = (0, start) #start에서 start까지 가는 비용이 0, 즉, 시작점

while D:
    v, (w, u) = D.popitem() #최소 힙에서 w값이 가장 작은 아이템 불러오기(heapdict 특성상 자동호됨)
    comp.add(v) #내륙 확정

    if u != v: #시작점일 때는 간선확정하지 말고 시작점이 아닐때만 간선 확정
        mst.append((u, v, w))

    for adj, weight in g[v].items(): #방금 확정된 점과 연결된 간선 정보 가져와서 루프 돌리기
        # 이미 내륙이면 무시
        if adj in comp: continue
        # 새로 추가할 정점 까지의 거리 정보가 이미 있을 때, 해당 거리보다 불러온 거리가 더 크면 무시
        if adj in D and D[adj][0] < weight : continue
        # 즉, 기존 간선보다 가깝거나 내륙에 없던 점으로 이어지는 간선이면 추가
        D[adj] = weight, v

#===========TSP 시작===============
#w 정보가 필요 없으므로 key값으로만 집합 생성
mg = {u: set() for u in range(num_vertex)}
for u, v, w in mst:
    mg[u].add(v)
    mg[v].add(u)

# print("MST 간선 그래프 리스트:")
# print_dict(mg)

#sequence 생성
seq = [start]
current = start
while True:
    if not mg[current] : break #더 이상 갈 곳이 없으면 멈추기

    for k in mg[current]:
        if k not in seq:    #아직 방문하지 않은 점이면 갈 곳으로 선정
            visit = k
            break
    else:   #break를 하지않고 온전히 실행된 후에 나오면 실행(파이썬의 for-else문)
        visit = list(mg[current])[0]

    mg[current].remove(visit) #선택한 점은 재방문을 막기 위해 삭제한다
    seq.append(visit)   #방문할 정점들에 추가한다
    current = visit

#중복 방문이 있는 경로 출력
print("-- Route through MST --")
print(seq)

#===========중복 방문 삭제============
index = 0
visited = set()

while index < len(seq):
    current = seq[index]
    if current in visited:  #방문한 점일때,
        seq.pop(index)  #seq에서 현재 점 삭제
        #pop으로 이미 인덱스가 이동됨
    else:   #방문한 점이 아닐 때,
        visited.add(current)   #방문한 점으로 기록
        index += 1  #다음 점으로 이동

#루프 과정에서 마지막 시작점으로 돌아오는 요소도 삭제됨
seq.append(start) #삭제된 시작점을 다시 추가

#중복방문을 제거한 루트 출력
print("-- Remove duplicated root --")
print(seq)