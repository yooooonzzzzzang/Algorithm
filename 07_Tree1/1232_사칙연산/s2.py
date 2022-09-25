import sys

sys.stdin = open('input.txt', encoding='utf-8')
def cal(v):
    if v !='0':
        cal(ch1[v])
        cal(ch2[v])
        if tree[v] =='+':
            tree[v] = int(tree[ch1[v]]) + int(tree[ch2[v]])
        elif tree[v] == '-':
            tree[v] = int(tree[ch1[v]]) - int(tree[ch2[v]])
        elif tree[v] == '*':
            tree[v] = int(tree[ch1[v]]) * int(tree[ch2[v]])
        elif tree[v] == '/':
            tree[v] = int(tree[ch1[v]]) // int(tree[ch2[v]])

for t in range(1, 11):
    n = int(input())
    tree = ['0'] * (n+1)
    ch1 = ['0'] * (n+1)
    ch2 = ['0'] * (n+1)
    for i in range(1,n+1):
        arr = input().split()
        # 정점이 숫자일때
        if len(arr) == 2:
            tree[int(arr[0])] = int(arr[1])
        # 정점이 연산자일때
        else:
            tree[int(arr[0])] = arr[1]
            ch1[int(arr[0])] = int(arr[2])
            ch2[int(arr[0])] = int(arr[3])
    print(tree)
    print(ch1)
    print(ch2)
    cal(1)
    print(f'#{t} {tree[1]}')
