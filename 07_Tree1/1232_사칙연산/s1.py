import sys

sys.stdin = open('input.txt')
def tree_cal(n):    # 후위순회 L R V(계산해주기)
    if n:
        tree_cal(ch1[n])
        tree_cal(ch2[n])
        if tree[n] == '-':
            tree[n] = int(tree[ch1[n]]) - int(tree[ch2[n]])
        elif tree[n] == '+':
            tree[n] = int(tree[ch1[n]]) + int(tree[ch2[n]])
        elif tree[n] == '*':
            tree[n] = int(tree[ch1[n]]) * int(tree[ch2[n]])
        elif tree[n] == '/':
            tree[n] = int(tree[ch1[n]]) // int(tree[ch2[n]])


for t in range(1, 11):
    N = int(input())    # 정점의 개수
    tree = [0] * (N + 1)
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)

    for i in range(N):
        arr = input().split()
        # 트리 만들어주기
        if len(arr) == 2:   # 정점이 정수
            tree[int(arr[0])] = int(arr[1])
        else:               # 정점이 연산자
            tree[int(arr[0])] = arr[1]
            ch1[int(arr[0])] = int(arr[2])
            ch2[int(arr[0])] = int(arr[3])
    root = 1
    tree_cal(root)
    print(f'#{t} {tree[root]}')