import sys

sys.stdin = open('sample_input.txt', encoding='utf-8')

for t in range(1, int(input()) + 1):
    n,m,l = map(int, input().split())
    tree = [0] * (n+1)
    for i in range(m):
        num, val = map(int,input().split())
        tree[num] = val
        while num != 0:
            num = num // 2
            tree[num] += val


    print(f'#{t} {tree[l]}')