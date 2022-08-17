import sys

sys.stdin = open('input.txt', encoding='utf-8')

for t in range(1, int(input()) + 1):
    print(f'#{t} ')
    N = int(input())

    pascal = [[1],[1,1]]
    for i in range(2, N):
        for j in range(N)
        temp = [1, pascal[i-1] + pascal[i], 1]

