'''
2
2 1 3

3
1 6 4 3 5 2 7
'''
# 중위트리의 값이 나열되어있음
# 가장 가운데 값이 루트 노드
# 나머지 서브트리의 가운데 루트를 찾는 것을 반복 후 레벨 별 저장
def find_root(v):
    global k
    if v!= 0:
        v //2
        find_root()
        find_root()



k = int(input())
tree = list(map(int, input().split()))
root = tree[len(tree)//2]
find_root(root)
