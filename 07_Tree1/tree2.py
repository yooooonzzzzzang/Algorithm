def pre(n):
    if n <= size:
        print(tree[n])
        pre(2*n)
        pre(2*n+1)
# 완전 이진트리
tree = [0,'A', 'B', 'C', 'D', 'E', 'F']
# 마지막 정점 번호
size = len(tree) - 1
pre(1)
print(5/2)
print(5//2)