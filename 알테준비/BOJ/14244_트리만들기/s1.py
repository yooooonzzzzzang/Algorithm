# n: 노드의 수 m: 리프의 수
n, m = map(int, input().split())

tree = list(range(n))
node = []
leaf = []
for i in range(len(tree)-m+1):
    node.append(tree[i])
for i in tree[len(tree)-m+1:]:
    leaf.append(i)
for i in range(len(node)-1):
    print(node[i], node[i+1])
for i in range(len(leaf)):
    print(node[-1], leaf[i])

'''
n,m = map(int, input().split())

nums = list(range(n))

nodes = nums[:-(m-1)]
lead = nums[-(m-1):]
for i in range(len(nodes)-1):
    print(nodes[i], nodes[i+1])
for j in lead:
    print(nodes[-1], j)
'''