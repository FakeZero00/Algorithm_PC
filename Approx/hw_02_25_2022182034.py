from welzl import welzl
from random import randint as rint, seed
from heapdict import heapdict
from math import sqrt

seed(20251202)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self): #문자열 변환될 때, 쓰이는 생성자
        return f'({self.x}, {self.y})'

def dist(p1, p2):
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def dist_sq(p1, p2):
    return (p1.x - p2.x)**2 + (p1.y - p2.y)**2

K = 5 # 클러스터 개수
points = [Point(rint(10, 99), rint(10, 99)) for _ in range(20)]
print(points)

centers = []
D = heapdict()

for k in range(K):
    if k == 0:
        center = rint(0, len(points)-1)
    else:
        center, _ = D.popitem()
    centers.append(center)
    print(f'center: {center}')

    #for i, pt in points.enumerate:
    for i in range(len(points)):
        dsq = dist_sq(points[center], points[i])

        # 저장을 음수로 했기 때문에 -1을 곱해줘야 양수 dsq와 비교할 수 있다
        if not i in D or dsq < -D[i][0]:
            D[i] = -dsq, center
        print(f'{i=} {dsq=:.2f} {-D[i][0]=} {D[i][1]=}')

print(f'centers: {centers}')
clusters = {center : [] for center in centers}
print(f'clusters: \n{clusters}')

for i in range(len(points)):
    _, which_center = D[i]
    clusters[which_center].append(points[i])

max_r = 0
for center, point in clusters.items():
    x, y, r = welzl(point)
    max_r = max(r, max_r)
    print(f'center {center} :')
    print(f'points: {point}')
    print(f'welzl circle: x:{x:.1f} y:{y:.1f} r:{r:.1f}\n')
print(f'max_r: {max_r:.1f}')