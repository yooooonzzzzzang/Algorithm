import sys

sys.stdin = open('sample_input.txt', encoding='utf-8')
def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])  # 경로 압축(Path compression)
    return parent[node]


for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    edges = []  # 연결 정보 및 비용을 저장할 리스트
    for _ in range(m):
        s, e, w = map(int, input().split())  # 시작 정점, 도착 정점, 비용
        edges.append((w, s, e))  # 비용, 시작, 도착 순으로 리스트에 저장

    edges.sort()  # (중요) 최소 비용의 간선부터 차례로 검사하기 위해 비용을 기준으로 오름차순 정렬
    parent = list(range(n + 1))  # 대표값을 저장할 리스트
    counts = 0  # MST의 간선 개수 (정점 - 1 개가 되면 종료를 하기 위함)
    cost = 0  # MST의 가중치 총합(== 최소 비용)

    for dist, x, y in edges:
        x_root, y_root = find_set(x), find_set(y)  # x와 y의 각각 대표값
        if x_root != y_root:  # 사이클이 아니면
            parent[y_root] = x_root  # union
            cost += dist  # 비용 누적
            counts += 1  # 간선의 개수 세기

            if counts >= n:  # 간선의 최대 개수는 정점(n+1개) - 1 이므로 break
                break

    print(f'#{t} {cost}')