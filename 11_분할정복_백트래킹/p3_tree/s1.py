def preorder(v):
    if v > 0:
        print(v, end=' ')
        preorder(ch1[v])
        preorder(ch2[v])
def inorder(v):
    if v > 0:
        inorder(ch1[v])
        print(v, end=' ')
        inorder(ch2[v])
def postorder(v):
    if v > 0:
        postorder(ch1[v])
        postorder(ch2[v])
        print(v, end=' ')

v, e = map(int, input().split())
ch1 = [0] * (v + 1)
ch2 = [0] * (v + 1)



arr = list(map(int, input().split()))
print(arr)
for i in range(e):
    p, c = arr[i * 2], arr[i * 2 + 1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

print("전위 순회 : ", end='')
preorder(1)
print()
print("중위 순회 : ", end='')
inorder(1)
print()
print("후위 순회 : ", end='')
postorder(1)
print()