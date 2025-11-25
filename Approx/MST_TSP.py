from random import randint
from heapdict import heapdict
import data_sample_cities as dsc

class MstTsp:
    def __init__(self, cities, edges):
        self.cities = cities
        self.n_cities = len(cities)
        self.edges = edges

    def build_graph(self, edges):
        g = {u: dict() for u in range(self.n_cities)}
        for u, v, w in edges:
            g[u][v] = w
            g[v][u] = w
        return g

    def main(self):
        self.start_index = randint(0, self.n_cities-1)
        self.g = self.build_graph(self.edges)
        self.mst()
        self.mg = self.build_graph(self.mst_edges)
        self.tsp()
        print(self.g)

    def mst(self):
        self.completed = set()
        self.completed.add(self.start_index)  # 시작점을 완성집합에 넣어둔다
        self.weights = heapdict()
        self.weights[self.start_index] = 0  # 시작점까지의 거리 0 을 넣고 최초꺼낼때 나오도록 한다
        self.origins = dict()
        self.origins[self.start_index] = self.start_index  # 거쳐 가는 점 정보에 같은 수를 넣어서 출발지로 삼는다
        self.mst_edges = []  # 결과를 저장할 Edge List

        while self.weights:
            v, w = self.weights.popitem()  # 알려진 거리가 가장 가까운 점(v)과 거리(w) 를 얻는다
            u = self.origins[v]  # v 에 가려면 u 를 들러서 가야 한다는 것을 알아낸다
            if u != v:  # v 가 출발점이 아니라면
                self.mst_edges.append((u, v, w))  # (u,v,w) 를 MST 에 추가한다
                self.completed.add(v)

            for adj, weight in self.g[v].items():  # 지금 확정되는 점 v 주위의 점들 adj 들에 대하여
                if adj in self.completed: continue  # 이미 완성집합에 들어있으면 무시한다
                if adj in self.weights and self.weights[adj] < weight: continue  # 거리정보가 있는데 이미 가까우면 무시한다
                self.weights[adj] = weight  # adj 까지 가는 가까운 거리는 weight 이며
                self.origins[adj] = v  # adj 까지 가려면 v 를 통해서 가야 한다

    def tsp(self):
        self.make_sequence()
        self.find_shortcut()

    def make_sequence(self):
        self.seq = [self.start_index]  # 방문할 정점들을 기록
        current = self.start_index
        while True:
            if current == self.start_index and not self.mg[self.start_index]:
                break  # 시작위치에 돌아왔을 때 더이상 갈 곳이 없으면 그만한다
            adjs = self.mg[current].keys()  # 현재 점의 주변 점들이 남아있는지 확인한다
            visit = None
            for k in adjs:
                if visit == None: visit = k  # 첫번째 점을 우선 선택해 둔다
                if k not in self.seq:  # 아직 방문하지 않은 점이면 선택한다
                    visit = k
                    break
            self.mg[current].pop(visit)  # 선택한 점은 재방문을 막기 위해 삭제한다
            self.seq.append(visit)  # 방문할 정점들에 추가한다
            current = visit  # 선택한 점으로 진행한다

    def find_shortcut(self):
        visited = set()  # 이미 방문한 점들의 집합
        index = 0
        while index < len(self.seq):  # 중복된 점이 없을때까지 진행
            current = self.seq[index]
            if current in visited:  # 방문했던 점이라면
                self.seq.pop(index)  # 현재 점은 삭제한다
            else:  # 그렇지 않다면 (방문 안한 점이면)
                visited.add(current)  # 방문한 점으로 기록하고
                index += 1  # 다음 점으로 넘어간다
        self.seq.append(self.start_index)

alg = MstTsp(dsc.cities, dsc.edges)
alg.main()