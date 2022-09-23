'''
2
2 1 3

3
1 6 4 3 5 2 7
'''
# 인풋값은 중위순회한 값이 나열되어있음
#  -> 가장 가운데 값이 루트 노드
# 나머지 서브트리의 가운데 루트를 찾는 것을 반복하고 같은 레벨끼리 배열에 넣어줌
def find_root(arr, depth):
    if depth == k:
        return
    mid = len(arr)//2
    result[depth].append(arr[mid])
    depth += 1
    find_root(arr[:mid], depth)
    find_root(arr[mid+1:], depth)


k = int(input())
tree = list(map(int, input().split()))
result = [[] for _ in range(k)]

find_root(tree, 0)
for line in result:
    print(*line)