import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    arr =[[0]*N for _ in range(N)]






    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()