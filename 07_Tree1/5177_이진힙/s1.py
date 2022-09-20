import sys

sys.stdin = open('sample_input.txt')
def heap_min(v):
    global last
    last += 1  # 마지막 노드 추가
    tree[last] = v
    child = last
    parent = child // 2

    # 부모가 0이 아니고, 부모 > 자식이면 자리 바꿈
    while parent and tree[parent] > tree[child]:
        tree[parent], tree[child] = tree[child], tree[parent]

        child = parent      # 위로 올라가기 위해서
        parent = child // 2 # 부모도 위로 올라간걸로 바꿔줌


for t in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (N + 1)
    last = 0    # 마지막 노드인덱스
    result = 0

    for i in arr:
        heap_min(i)

    # 조상노드 합 구하기
    while N:    # N 이 0 이 아닌동안
        N=N//2
        result += tree[N]
    print(f'#{t} {result}')