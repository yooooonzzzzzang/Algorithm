import sys

sys.stdin = open('input.txt', encoding='utf-8')

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def delta(x, y):
    global result
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<= nx < n and 0 <= ny < n:
            result += abs(arr[nx][ny]-arr[x][y])
for t in range(1, int(input()) + 1):
    n = int(input())
    result = 0
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            delta(i,j)
    print(f'#{t} {result}')

