'''
정점 번호 1 ~ (E + 1)
간선 수
부모- 자식 순
- 3을 루트로 하는 서브트리에 속한 정점의 개수는?

13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0: # 부모가 없으면 root
            return i

def preorder(n): # V L R
    global cnt
    if n :  # n!=0
        # print(n)    # visit(n)
        cnt += 1
        # cnt = n   # 마지막 정점 프린트, 마지막은 더이상 덮어쓸수없게 됨
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n): # L V R
    if n:
        inorder(ch1[n])
        print(n)
        inorder(ch2[n])

def postorder(n):   # L R V
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)

V = int(input())    # 정점 개수, 마지막 정점번호
arr = list(map(int, input().split()))
E = V - 1
root = 1
# 부모를 인덱스로 자식 번호 저장
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)
# 자식을 인덱스로 부모 번호 저장
par = [0] * (V + 1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0: # 자식이 없으면
        ch1[p] = c  # 자식1로 저장
    else:
        ch2[p] = c
    par[c] = p
root = find_root(V)
cnt = 0
preorder(3)
print(cnt)

