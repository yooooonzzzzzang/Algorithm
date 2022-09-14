import sys

sys.stdin = open('sample_input.txt', encoding='utf-8')
def preorder(n): # V L R
    global cnt
    if n:  # n!=0
        cnt += 1
        preorder(ch1[n])
        preorder(ch2[n])

for t in range(1, int(input()) + 1):
    E, N = map(int, input().split())        # 간선과 루트
    arr = list(map(int, input().split()))
    V = E + 1
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
    print(ch1)
    print(ch2)
    root = N
    cnt = 0
    preorder(root)
    print(f'#{t} {cnt}')