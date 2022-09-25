'''
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
'''
def pre(v):
    if v != '0':
        print(v, end='')
        #  tree 리스트 내부에 v값의 index를 보내주면 그 index의 자식 노드를 확인하고 순회
        pre(ch1[tree.index(v)])
        pre(ch2[tree.index(v)])

def inorder(v):
    if v != '0':
        inorder(ch1[tree.index(v)])
        print(v, end='')
        inorder(ch2[tree.index(v)])

def postorder(v):
    if v != '0':
        postorder(ch1[tree.index(v)])
        postorder(ch2[tree.index(v)])
        print(v, end='')

n = int(input())    # 노드의 개수
tree = ['0'] * (n + 1)
ch1 = ['0'] * (n + 1)
ch2 = ['0'] * (n + 1)
for i in range(1, n+1):
    arr = input().split()
    for idx,j in enumerate(arr):
        if j == '.':
            pass
        else:
            if idx == 0:
                tree[i] = j
            elif idx == 1:
                ch1[i] = j
            else:
                ch2[i] = j


pre('A')
print()
inorder('A')
print()
postorder('A')
print(tree)